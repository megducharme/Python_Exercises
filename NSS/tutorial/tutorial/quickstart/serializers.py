from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class HockeyPlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyPlayer
        exclude = ()

class HockeyTeamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyTeams
        fields = ('teamname', 'city', 'coach', 'logo', 'mascot')
