from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer): # RoomSerializer is a class that inherits from the ModelSerializer class
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')