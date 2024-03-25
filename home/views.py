from django.shortcuts import render 
from rest_framework import generics 
from rest_framework import status 
from .serializers import ChatSerializers 
from .models import Chat,User
from django.db.models import OuterRef, Subquery, Q

# Create your views here.  

class MyInbox(generics.ListAPIView): 
    serializer_class = ChatSerializers 
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        messages = Chat.objects.filter(
            id__in =Subquery(
                User.objects.filter(
                    Q(sender__receiver=user_id)|
                    Q(receiver__sender=user_id)                    
                ).distinct().annotate(
                    last_msg = Subquery(
                        Chat.objects.filter(
                            Q(sender=OuterRef('id'),receiver=user_id)|
                            Q(receiver=OuterRef('id'),sender=user_id)
                        ).order_by("-id")[:1].values_list("id",flat=True)
                    )
                ).values_list("last_msg",flat=True)
            )
        ).order_by("-id")
        return messages


class GetMessages(generics.ListAPIView): 
    serializer_class = ChatSerializers 
    
    def get_queryset(self):
        sender_id   = self.kwargs['sender_id']
        receiver_id = self.kwargs['receiver_id'] 
        
        messages = Chat.objects.filter(
            sender__in = [sender_id,receiver_id],
            receiver__in = [receiver_id,sender_id]
        )
        return messages  
    
    
class SendMessages(generics.CreateAPIView): 
    serializer_class = ChatSerializers
    
    
