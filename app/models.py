from django.db import models
from company.models import Job
from django.contrib.auth.models import User

# Create your models here.
class Like_job(models.Model):
    id_like_job = models.BigAutoField(primary_key=True)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_like_job
    
    


    
