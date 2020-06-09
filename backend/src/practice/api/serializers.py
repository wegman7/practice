from django.contrib.auth.models import User
from rest_framework import serializers

from practice.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('__all__')