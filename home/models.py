from django.db import models 
from Account.models import Profile,User
# Create your models here. 

class Chat(models.Model): 
    user      = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    sender    = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    message   = models.CharField(max_length=10000)   
    file      = models.FileField(upload_to='chat_files',blank=True,null=True)
    is_read   = models.BooleanField(default=False)
    date      = models.DateTimeField(auto_now_add=True)  
    
    
    
    class Meta: 
        ordering = ['date'] 
        verbose_name = 'Message'  
        
        
    def __str__(self) -> str:
        return f"{self.sender} - {self.receiver} - {self.is_read}"
    
    @property 
    def sender_profile(self): 
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile 
    
    @property 
    def receiver_profile(self): 
        receiver_profile = Profile.objects.get(user=self.receiver)
        return receiver_profile  
    
    
    
        
        
    
    
     
    
