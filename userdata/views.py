import json

import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from userdata.models import UserProfile
from userdata.models import CitSciProject
from userdata.models import Citizen
from userdata.models import CitizenOpinion, OpinionQuestion, OpinionQuestionOption
from models import Reservation

from userdata.serializers import CitizenSerializer, OpinionQuestionSerializer, OpinionQuestionOptionSerializer
from userdata.serializers import CitizenOpinionSerializer
from userdata.serializers import ReservationSerializer, AvailabilitySerializer, DateAvailableSerializer
from availability import  Availability

from userdata.motionai import MotionAI

@api_view(['GET', 'POST'])
def reservations_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        r_data = request.data
        data = {
            'eventName': request.data.get('eventName'),
            'eventStartDate': request.data.get('eventStartDate'),
            'eventEndDate': request.data.get('eventEndDate'),
            'numberOfDevices': request.data.get('numberOfDevices'),
            'deliveryMethod': request.data.get('deliveryMethod'),
            'outDate': request.data.get('outDate'),
            'returnDate': request.data.get('returnDate'),
            'bookerName': request.data.get('bookerName'),
            'bookerEmail': request.data.get('bookerEmail'),
            'deliveryAddress': request.data.get('deliveryAddress'),
            'costCode': request.data.get('costCode'),
        }
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def _format_user_for_json_return(u):
    return {
        "username": u.username,
        "date_joined": u.date_joined.strftime("%c"),
        "groups": [{"name": g.name} for g in u.groups.all()],
        "nickname": UserProfile.get_or_create_for_user(u).nickname
    }


def api_user_list(request):
    users = User.objects.all()
    users_as_objects = [_format_user_for_json_return(u) for u in users]
    users_as_json = json.dumps(users_as_objects)
    return HttpResponse(content=users_as_json, content_type="application/json")


def api_user_details(request, user_id):
    if request.method == "GET":
        user = User.objects.get(id=user_id)
        user_as_object = _format_user_for_json_return(user)
        user_as_json = json.dumps(user_as_object)
        return HttpResponse(content=user_as_json, content_type="application/json")
    if request.method == "POST":
        raise NotImplementedError()


def api_citzens_list(request):
    citizens = Citizen.objects.all()
    return HttpResponse(citizens)


@api_view(['POST'])
def api_citzenopinion_get(request):
    if request.method == 'POST':
        r_data = request.data
        fn = r_data.get('full_name')
        data = {'full_name': request.data.get('full_name'), 'short_name': request.data.get('short_name')}
        serializer = CitizenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_opinionquestion_list(request):
    if request.method == 'GET':
        opinionquestions = OpinionQuestion.objects.all()
        serializer = OpinionQuestionSerializer(opinionquestions, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_citizen_opinion(request):
    if request.method == 'GET':
        citizen_opinions = CitizenOpinion.objects.all()
        serializer = CitizenOpinionSerializer(citizen_opinions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        r_data = request.data
        # data = {'user': request.data.get('user'),
        #         'project': request.data.get('project'),
        #         'confidence': request.data.get('confidence'),
        #         'question': request.data.get('question'),
        #         'answer_option': request.data.get('answer_option'),
        #         'answer_text': request.data.get('answer_text')}
        data = {'user': request.data.get('user'),
                'project': request.data.get('project'),
                'question': request.data.get('question'),
                'answer_option': request.data.get('answer_option'),
                'answer_text': request.data.get('answer_text')}
        serializer = CitizenOpinionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def stringToDate(dateString):
    dateBits = dateString.split('-')
    return datetime.date(int(dateBits[0]), int(dateBits[1]), int(dateBits[2]))


@api_view(['GET'])
def availability(request):
    if request.method == 'GET':
        availabilityJson = {u'availableQQQ': True}
        return Response(availabilityJson)

        # params = request.query_params
        # fromDate = stringToDate(params.get('fromDate'))
        # toDate = stringToDate(params.get('toDate'))
        # numberRequested = int(params.get('numberRequested'))
        #
        # av = Availability(True).CalculateAvailability(fromDate, toDate, numberRequested)
        #
        # serializer = AvailabilitySerializer(av, many=False)
        # return Response(serializer.data)

END_DATE_MODULEID = '259360'
CHECK_AVAILABILITY_MODULEID = '272607'

@api_view(['POST'])
def webhook(request):
    if request.method == 'POST':
        requestData = request.data
        print requestData
        reqInfo = requestData['direction'] + ' - ' + requestData['moduleID']
        if 'replyData' in requestData:
            pass
            reqInfo += ' - ' + requestData['replyData']
        # print str(requestData['direction'] == 'out')
        if (requestData['moduleID'] == END_DATE_MODULEID and requestData['direction'] == 'in') or \
                (requestData['moduleID'] == CHECK_AVAILABILITY_MODULEID and requestData['direction'] == 'out'):
            reqInfo += ' - availability: '
            deviceRequest = MotionAI.checkAvailabilityFromBotData()
            print deviceRequest
            availability = Availability.CalculateAvailability(deviceRequest['fromDate'], deviceRequest['toDate'], deviceRequest['numberRequested'])
            if availability.available == True:
                pass
            else:
                pass

            # returnData = { "key1": 'wait and see', "key2": "value2" }
        # for r in returnData.values():
        #     print r
        returnData = {'key1': reqInfo}
        return Response(data=returnData, content_type='application/json')

@api_view(['GET', 'POST'])
def citizen_list(request):
    if request.method == 'GET':
        citizens = Citizen.objects.all()
        serializer = CitizenSerializer(citizens, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        r_data = request.data
        fn = r_data.get('full_name')
        data = {'full_name': request.data.get('full_name'), 'short_name': request.data.get('short_name')}
        serializer = CitizenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def citizen_test(request):
    if request.method == 'GET':
        citizens = Citizen.objects.all()
        serializer = CitizenSerializer(citizens, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def citizen_detail(request, pk):
    try:
        citizen = Citizen.objects.get(pk=pk)
    except Citizen.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CitizenSerializer(citizen, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        citizen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


