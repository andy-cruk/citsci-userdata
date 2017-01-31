import urllib2
import json

DEVICECOUNT_MODULE_ID = 250213
STARTDATE_MODULE_ID = 259360
ENDDATE_MODULE_ID = 259365

NGROK_URL = 'http://b2b093da.ngrok.io'
MOTIONAI_URL = 'https://api.motion.ai/1.0/getConversations?key=8bfbd77cb45cb47812bbaee4063351bc'

class MotionAI(object):

    @staticmethod
    def openURL(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'application/json',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
        response = urllib2.urlopen(req).read()
        return response

    @staticmethod
    def openJsonURL(url):
        return json.loads(MotionAI.openURL(url))

    @staticmethod
    def getSessionIdFromBot(url):
        jsonData = MotionAI.openJsonURL(url)
        return jsonData['messages'][0]['session']

    @staticmethod
    def GetSessionResponsesFromBot(sessionId):
        url = MOTIONAI_URL + '&direction=in&session=' + sessionId
        return MotionAI.openJsonURL(url)

    @staticmethod
    def checkAvailabilityFromBotData():
        url = MOTIONAI_URL + '&module=259361&direction=in'
        sessionId = MotionAI.getSessionIdFromBot(url)
        jsonData = MotionAI.getSessionResponsesFromBot(sessionId)
        print jsonData
        messages = jsonData['messages']
        for message in messages:
            moduleId = message['module']
            result = message['result']
            # print 'module:' + str(message['module']) + '  result:' + str(message['result'])
            if moduleId == DEVICECOUNT_MODULE_ID:
                deviceCount = result
                # print 'devices: ' + str(deviceCount)
            elif moduleId == STARTDATE_MODULE_ID:
                startDate = result[0:10]
                # print 'start: ' + str(startDate)[0:10]
            elif moduleId == ENDDATE_MODULE_ID:
                endDate = result[0:10]
                # print 'end: ' + str(endDate)[0:10]

        # for exteranl calls
        url = NGROK_URL + '/availability?fromDate=' + startDate + '&toDate=' + endDate + '&numberRequested=' + str(deviceCount)
        # print url
        availabilityJson = MotionAI.openJsonURL(url)

        return availabilityJson


    @staticmethod
    def getDeviceRequestFromBotData():
        url = MOTIONAI_URL + '&module=259361&direction=in'
        sessionId = MotionAI.getSessionIdFromBot(url)
        jsonData = MotionAI.getSessionResponsesFromBot(sessionId)
        print jsonData
        messages = jsonData['messages']
        for message in messages:
            moduleId = message['module']
            result = message['result']
            # print 'module:' + str(message['module']) + '  result:' + str(message['result'])
            if moduleId == DEVICECOUNT_MODULE_ID:
                deviceCount = result
                # print 'devices: ' + str(deviceCount)
            elif moduleId == STARTDATE_MODULE_ID:
                startDate = result[0:10]
                # print 'start: ' + str(startDate)[0:10]
            elif moduleId == ENDDATE_MODULE_ID:
                endDate = result[0:10]
                # print 'end: ' + str(endDate)[0:10]

        return {'fromDate' : startDate, 'toDate' : endDate, 'numberRequested' : str(deviceCount) }
