from rest_framework import serializers
from .models import Manager
from django.contrib.auth.models import User

class EmpSer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    dept=serializers.CharField()
    qualification=serializers.CharField()


class ManagerModelSer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields="__all__"

class UserModelSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)