from rest_framework import serializers

from userdata.models import UserProfile, OpinionQuestion, OpinionQuestionOption
from userdata.models import CitSciProject
from userdata.models import Citizen
from userdata.models import CitizenOpinion
from models import Reservation

class ReservationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'eventName', 'eventStartDate', 'eventEndDate', 'numberOfDevices',
                  'deliveryMethod', 'outDate', 'returnDate', 'bookerName',
                  'bookerEmail', 'deliveryAddress', 'costCode')

class AvailabilitySerializer (serializers.Serializer):
    available = serializers.BooleanField()
    # dateAvailability = DateAvailableSerializer(required=False, many=True)


class DateAvailableSerializer(serializers.Serializer):
    date = serializers.DateField()
    numberAvailable = serializers.ImageField()


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('id', 'short_name', 'full_name')


class OpinionQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpinionQuestionOption
        fields = ('id', 'text', 'sequence')


class OpinionQuestionOptionField(serializers.RelatedField):
    def to_representation(self, value):
        return OpinionQuestionOptionSerializer(value).data


class OpinionQuestionSerializer(serializers.ModelSerializer):
    options = OpinionQuestionOptionField(many=True, read_only=True)

    class Meta:
        model = OpinionQuestion
        fields = ('id', 'text', 'sequence', 'required', 'question_type', 'options')

class CitizenOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenOpinion
        # fields = ('user', 'datetime', 'project', 'question', 'answer_option', 'answer_text')
        fields = ('user', 'datetime', 'project', 'question', 'answer_option', 'answer_text')