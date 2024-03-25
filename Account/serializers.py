from .models import Profile 
from rest_framework.serializers import ModelSerializer 


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile 
        fields = ['id','user','profile_picture']
        
        

class ProfileViewSerializers(ModelSerializer): 
    class Meta: 
        model = Profile 
        fields = '__all__'
        