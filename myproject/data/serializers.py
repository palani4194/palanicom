from rest_framework import serializers
from . models import AdultData

from django.contrib.auth.models import User, Group

class adultserializers(serializers.ModelSerializer):
    class Meta:
        model = AdultData
        fields ='__all__'
