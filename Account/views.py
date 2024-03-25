from django.shortcuts import render
from rest_framework import generics  
from .models import Profile  
from .serializers import ProfileViewSerializers 
from rest_framework.permissions import IsAuthenticated
from django.db.models import OuterRef, Subquery, Q 
from rest_framework.response import Response 
from rest_framework import status
# Create your views here. 

class ProfileUpdateAndDelete(generics.RetrieveUpdateAPIView): 
    serializer_class = ProfileViewSerializers 
    queryset = Profile.objects.all()  
    permission_classes = [IsAuthenticated] 
    
    
#search a user 
class SearchUser(generics.ListAPIView): 
    serializer_class = ProfileViewSerializers 
    queryset = Profile.objects.all() 
    
    def list(self, request, *args, **kwargs): 
        username = self.kwargs['username'] 
        logged_in_user = self.request.user 
        
        users = Profile.objects.filter(
            Q(user__username__icontains=username)|
            Q(user__email__icontains=username)|
            Q(user__first_name__icontains=username)|
            Q(user__last_name__icontains=username) & 
            ~Q(user=logged_in_user)
        ) 
        
        if not users.exists(): 
            return Response(
                {"details":"User is not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
         
        serializers = self.get_serializer(users,many=True)
        return Response(serializers.data)
    
    