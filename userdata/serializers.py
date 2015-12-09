from rest_framework import serializers

from userdata.models import UserProfile, OpinionQuestion, OpinionQuestionOption
from userdata.models import CitSciProject
from userdata.models import Citizen
from userdata.models import CitizenOpinion

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
