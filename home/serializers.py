from .models import Chat 
from rest_framework.serializers import ModelSerializer  
from Account.serializers import ProfileSerializers



class ChatSerializers(ModelSerializer): 
    sender_profile   = ProfileSerializers(read_only=True)
    receiver_profile = ProfileSerializers(read_only=True)
    class Meta: 
        model = Chat 
        fields = ['id','user','sender','sender_profile','receiver','receiver_profile','message','file','is_read','date']
        
        
    