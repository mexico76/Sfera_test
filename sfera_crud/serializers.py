from django.contrib.auth.models import User
from rest_framework import serializers

class CRUDUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'date_joined', 'id']