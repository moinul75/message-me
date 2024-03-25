from django.urls import path  
from .views import ProfileUpdateAndDelete,SearchUser

urlpatterns = [
    path('profile/<int:pk>/',ProfileUpdateAndDelete.as_view(),name='prifile-update'),
    path('search/<username>/',SearchUser.as_view(),name='search-user')
]
