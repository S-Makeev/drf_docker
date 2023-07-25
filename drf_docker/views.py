from rest_framework import generics
from .serializer import ProfileSerializer
from .models import EmployeeProfile

class ProfileList(generics.ListCreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = ProfileSerializer