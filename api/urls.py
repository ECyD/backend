from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'user/$', UserView.as_view()),
]