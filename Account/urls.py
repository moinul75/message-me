from django.urls import path  
from .views import ProfileUpdateAndDelete,SearchUser,CustomTokenObtainPairView, CustomTokenRefreshView,UserRegistrationView

urlpatterns = [
    path('profile/<int:pk>/',ProfileUpdateAndDelete.as_view(),name='prifile-update'),
    path('search/<username>/',SearchUser.as_view(),name='search-user'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
