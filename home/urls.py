from django.urls import path  
from .views import MyInbox,GetMessages,SendMessages


urlpatterns = [
    path('messages/<user_id>/',MyInbox.as_view(),name="my-inbox"),
    path('get-messages/<sender_id>/<receiver_id>/',GetMessages.as_view(),name="get-messages"),
    path('send-messages/',SendMessages.as_view(),name="send-messages"), 
]
