from rest_framework import viewsets

from .serializers import ProfileSerializer
from practice.models import Profile

class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()