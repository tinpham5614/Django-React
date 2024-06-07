from django.db import models
import string
import random

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code
# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) # code is the room code
    host = models.CharField(max_length=50, unique=True) # host is the user who created the room
    guest_can_pause = models.BooleanField(null=False, default=False) # guest_can_pause is a boolean field that determines if the guest can pause the music
    votes_to_skip = models.IntegerField(null=False, default=1) # votes_to_skip is an integer field that determines how many votes are needed to skip a song
    created_at = models.DateTimeField(auto_now_add=True) # created_at is a date time field that stores the date and time the room was created
    