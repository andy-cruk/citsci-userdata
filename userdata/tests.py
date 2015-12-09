import json
from unittest import TestCase

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from userdata import views
from userdata.models import OpinionQuestion, QUESTION_TYPES, OpinionQuestionOption
from userdata.serializers import OpinionQuestionSerializer, OpinionQuestionOptionSerializer


class UserApiTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def create_test_user(self):
        return User.objects.create_user(username="test01", email="test01@test.com", password="password")

    def check_user_object_has_properties(self, user_data):
        for key in ("username", "date_joined", "groups", "nickname"):
            self.assertTrue(key in user_data)

    def test_api_user_list(self):

        def make_list_users_api_request():
            relative_url = reverse(views.api_user_list)
            request = self.factory.get(relative_url)
            response = views.api_user_list(request)
            return response

        response = make_list_users_api_request()
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertEquals(response_json, [])

        user01 = self.create_test_user()
        response = make_list_users_api_request()
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertTrue(type(response_json) == list)
        self.assertTrue(len(response_json) == 1)
        user_data = response_json[0]
        self.assertTrue(user_data['username'] == user01.username)
        self.check_user_object_has_properties(user_data)
        user01.delete()

    def test_api_user_details(self):

        def make_user_detail_api_request(user_id):
            relative_url = reverse(views.api_user_details, args=[user_id])
            request = self.factory.get(relative_url)
            response = views.api_user_details(request, user_id)
            return response

        with self.assertRaises(User.DoesNotExist):
            response = make_user_detail_api_request("1")

        user = self.create_test_user()
        response = make_user_detail_api_request(user.id)
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)
        self.check_user_object_has_properties(response_json)
        user.delete()


class OpinionQuestionTests(TestCase):

    def setUp(self):
        [oq.delete() for oq in OpinionQuestion.objects.all()]
        [oqo.delete() for oqo in OpinionQuestionOption.objects.all()]

    def _delete_basic_oq(self, oq):
        oq.delete()
        # Check there are no OQ's
        self.assertEquals(OpinionQuestion.objects.count(), 0)

    def _create_basic_oq(self):
        # Check there are no OQ's
        self.assertEquals(OpinionQuestion.objects.count(), 0)
        # Add one
        oq = OpinionQuestion(
            text="test",
            question_type=1,
            sequence=1,
            required=True)
        oq.save()
        return oq

    def test_serializer_can_serialize_basic_question_properties(self):
        oq = self._create_basic_oq()
        self.assertEquals(OpinionQuestion.objects.count(), 1)
        serializer = OpinionQuestionSerializer(oq)
        serialized_data = serializer.data
        # serialized_data is a dict
        self.assertTrue(isinstance(serialized_data, dict))
        # check it has the same properties as the OQ
        # print(serialized_data)
        for prop, value in {'text': 'test', 'question_type': 1, 'sequence': 1, 'required': True}.items():
            self.assertEquals(serialized_data[prop], value)
        self._delete_basic_oq(oq)

    def test_serializer_can_serialize_related_entities(self):
        oq = self._create_basic_oq()
        oqo = OpinionQuestionOption(text='opt1', sequence=1)
        oqo.save()
        oq.options.add(oqo)
        self.assertEquals(oq.options.count(), 1)
        serializer = OpinionQuestionSerializer(oq)
        serialized_data = serializer.data
        self.assertTrue(isinstance(serialized_data['options'], list))
        self.assertEquals(len(serialized_data['options']), 1)
        self.assertEquals(serialized_data['options'][0], OpinionQuestionOptionSerializer(oqo).data)
        self._delete_basic_oq(oq)



class OpinionQuestionOptionTests(TestCase):

    def test_serializer(self):
        self.assertEquals(OpinionQuestionOption.objects.count(), 0)
        oqo = OpinionQuestionOption(text='test', sequence=1)
        oqo.save()
        self.assertEquals(OpinionQuestionOption.objects.count(), 1)
        serialized = OpinionQuestionOptionSerializer(oqo)
        serialized_data = serialized.data
        self.assertTrue(isinstance(serialized_data, dict))
        for prop, value in {'text': 'test', 'sequence': 1}.items():
            self.assertEquals(serialized_data[prop], value)
        oqo.delete()
        self.assertEquals(OpinionQuestionOption.objects.count(), 0)

