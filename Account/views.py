from django.shortcuts import render
from rest_framework import generics  
from .models import Profile  
from .serializers import ProfileViewSerializers,UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import OuterRef, Subquery, Q 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.  



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Assuming the request contains 'username' and 'password'
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access),
        })
        
class CustomTokenRefreshView(TokenRefreshView):
    pass  

class ProfileUpdateAndDelete(generics.RetrieveUpdateAPIView): 
    serializer_class = ProfileViewSerializers 
    queryset = Profile.objects.all()  
    permission_classes = [IsAuthenticated] 
    
    
#search a user 
class SearchUser(generics.ListAPIView): 
    serializer_class = ProfileViewSerializers 
    queryset = Profile.objects.all() 
    permission_classes = [IsAuthenticated] 
    
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
    
    