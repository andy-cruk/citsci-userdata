from django.contrib import admin

from .models import CitizenOpinion, Citizen, CitSciProject, OpinionQuestion, OpinionQuestionOption

admin.site.register(CitizenOpinion)
admin.site.register(Citizen)
admin.site.register(CitSciProject)
admin.site.register(OpinionQuestion)
admin.site.register(OpinionQuestionOption)