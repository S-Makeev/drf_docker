from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class EmployeeProfile(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=32)
    outside_contractor = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name