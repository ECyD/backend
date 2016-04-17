from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'user/$', UserView.as_view()),

    url(r'team/$', TeamView.as_view()),
    url(r'team/(?P<pk>[0-9]+)/$', TeamDetailView.as_view()),

    url(r'kid/$', KidView.as_view()),
    url(r'kid/(?P<pk>[0-9]+)/$', KidDetailView.as_view()),

    url(r'bitacora/$', BitacoraView.as_view()),
    url(r'bitacora/(?P<pk>[0-9]+)/$', BitacoraDetailView.as_view()),

    url(r'leader/$', LeaderView.as_view()),
    url(r'leader/(?P<pk>[0-9]+)/$', LeaderDetailView.as_view()),
]