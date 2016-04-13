from rest_framework import serializers
from user.models import *
from school.models import *

#----------DEFAULT----------#
class DefaultMyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_pic', 'school']

class DefaultTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'school']

class DefaultKidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = ['id', 'first_name', 'last_name']

class DefaultLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ['id', 'first_name', 'last_name', 'school']

class DefaultBitacoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitacora
        fields = ['id', 'date', 'assistance', 'week_talk']

#----------NORMAL----------#
