from django.conf.urls import patterns, include, url
from django.contrib import admin
from userdata import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'userdata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'reservations$', views.reservations_list),
    url(r'availability$', views.availability),
    url(r'webhook$', views.webhook),

    url(r'api/users/all$', views.api_user_list),
    url(r'api/users/(?P<user_id>\d+)$', views.api_user_details),

    url(r'api/citizenopinion/(?P<user_id>\d+)$', views.api_citzenopinion_get),

    url(r'^admin/', include(admin.site.urls)),

    url(r'api/citizens$', views.citizen_list),
    url(r'api/citizen/(?P<pk>\d+)$', views.citizen_detail),

    url(r'api/opinionquestions$', views.api_opinionquestion_list),

    url(r'api/citizenopinions$', views.api_citizen_opinion),

)
