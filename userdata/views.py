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
from userdata.models import CitizenOpinion

from userdata.serializers import CitizenSerializer

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


def api_citzenopinion_get(request, user_id):
    # user = User.objects.get(id=user_id)
    # opinions = CitizenOpinion.objects.get(user=user_id)
    return HttpResponse(user_id)


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


