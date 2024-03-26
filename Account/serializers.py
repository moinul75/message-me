from .models import Profile 
from rest_framework.serializers import ModelSerializer 
from django.contrib.auth.models import User 
from rest_framework import serializers

class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name'] 

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''), 
            last_name=validated_data.get('last_name', '')  
        )
        return user


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile 
        fields = ['id','user','profile_picture']
        
        

class ProfileViewSerializers(ModelSerializer): 
    class Meta: 
        model = Profile 
        fields = '__all__'
        