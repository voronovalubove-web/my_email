from django.db import models


class Letter(models.Model):
    sender = models.CharField(max_length=100)     
    recipient = models.CharField(max_length=100)   
    subject = models.CharField(max_length=200)     
    body = models.TextField()                      
    created_at = models.DateTimeField(auto_now_add=True) 
    is_read = models.BooleanField(default=False)   
    folder = models.CharField(max_length=20, default='inbox') 

    def __str__(self):
        return self.subject