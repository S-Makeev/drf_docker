from rest_framework import serializers
from.models import EmployeeProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'full_name', 'date_of_birth', 'position','outside_contractor', 'created_at')
        model = EmployeeProfile