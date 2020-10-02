from django.contrib.auth.models import User, Group
from rest_framework import serializers

from sports.api.models import Locations, Sites, Addresses, Events, ParticipantsEvents


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = '__all__'
        depth = 2


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth = 3


class ParticipantsEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantsEvents
        fields = '__all__'