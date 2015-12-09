from django.contrib.auth.models import User
from django.db import models

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

QUESTION_TYPES = (
    (1, 'Text'),
    (2, 'SingleOptionList'),
    (3, 'MultiOptionList'),
    (4, 'YesNo')
)

class OpinionQuestionOption(models.Model):
    text = models.CharField(max_length=100)
    sequence = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return self.text


class OpinionQuestion(models.Model):
    text = models.CharField(max_length=100)
    question_type = models.IntegerField(choices=QUESTION_TYPES)
    sequence = models.PositiveSmallIntegerField()
    required = models.BooleanField(default=False)
    options = models.ManyToManyField(OpinionQuestionOption)

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return self.text


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=1024)

    @classmethod
    def get_or_create_for_user(cls, user):
        """This is one way of getting a forigen key related object - using a class (static) method"""
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=user)
            profile.save()
        return profile


class CitSciProject(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id + ':' + self.name


class Citizen(models.Model):
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=20)
    projects = models.ManyToManyField(CitSciProject)

    class Meta:
        ordering = ['short_name']

    def __str__(self):
        return self.short_name


class CitizenOpinion(models.Model):
    user = models.ForeignKey(Citizen)
    datetime = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=20, default='')
    confidence = models.IntegerField()

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return '{0} {1}'.format(self.datetime.strftime(DATETIME_FORMAT), self.user)




