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
        fields = ['id', 'team_name', 'school', 'grade']

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
class MyUserSerializer(serializers.ModelSerializer):

    teams = DefaultTeamSerializer(many=True)

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_pic', 'school', 'teams']

class TeamSerializer(serializers.ModelSerializer):

    my_user = DefaultMyUserSerializer(many=False)
    kids = DefaultKidSerializer(many=True)
    leaders = DefaultLeaderSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'team_name', 'school', 'grade', 'my_user', 'kids', 'leaders']

class LeaderSerializer(serializers.ModelSerializer):

    team = DefaultTeamSerializer(many=False)

    class Meta:
        model = Leader
        fields = ['id', 'first_name', 'last_name', 'school', 'team']

class KidSerializer(serializers.ModelSerializer):

    team = DefaultTeamSerializer(many=False)
    bitacoras = DefaultBitacoraSerializer(many=True)

    class Meta:
        model = Kid
        fields = ['id', 'first_name', 'last_name', 'team', 'bitacoras']

class BitacoraSerializer(serializers.ModelSerializer):

    kid = DefaultKidSerializer(many=False)

    class Meta:
        model = Bitacora
        fields = ['id', 'date', 'assistance', 'week_talk', 'kid']
