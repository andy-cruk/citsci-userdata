import datetime
import urllib
import urllib2

from models import Reservation

class Availability(object):
    def __init__(self, available):
        self.available = available
        self.dateAvailability = [
            {'date': '20/12/2016', 'numberAvailable': 2}
        ]

    @staticmethod
    def CalculateAvailability(fromDate, toDate, numberRequested):
        initialAvailability = 3
        reservations = Reservation.objects.all()
        dateAvailability = []
        date = fromDate
        # initialise data availability array
        while(date <= toDate):
            dateAvailability.append([date, initialAvailability])
            date += datetime.timedelta(1)

        # now take account of existing reservations
        devicesAvailable = True
        for reservation in reservations:
            date = fromDate
            dateIndex = 0
            while (date <= toDate):
                if (date <= reservation.returnDate) and (date >= reservation.outDate):
                    dateAvailability[dateIndex][1] -= reservation.numberOfDevices
                    print '***'
                print date, dateAvailability[dateIndex][1]
                if (dateAvailability[dateIndex][1] < numberRequested):
                    devicesAvailable = False
                date += datetime.timedelta(1)
                dateIndex += 1

        print dateAvailability

        return Availability(available=devicesAvailable)

