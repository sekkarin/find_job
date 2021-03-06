from django.db import models
from django.contrib.auth.models import User
from app.models import *
# Create your models here.

class Type_job (models.Model):
    id_type = models.BigAutoField(primary_key=True)
    name_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_type

    
class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_company = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    discripts = models.CharField(max_length=300)
    welfare  = models.CharField(max_length=50)
    
    image = models.FileField(upload_to='media/img/company',default="None")
    # id_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    # id_job = models.IntegerField(default=0)
    def __str__(self):
        return self.name_company
class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_job =  models.CharField(max_length=100)
    date_post =  models.DateTimeField(auto_now=False)
    job_title = models.IntegerField()
    detial = models.CharField(max_length=100)
    property_job = models.CharField(max_length=50)
    job_application = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    salary = models.FloatField(default=0)
    # added = models.TimeField(auto_now=True, auto_now_add=True,default=0),
    id_type = models.ForeignKey(Type_job, on_delete=models.CASCADE)
    id_company  = models.ForeignKey(Company, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name_job

class Job_application(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="member_application")
    # job = models.ForeignKey(Job,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    
    # class Meta:
    #     verbose_name = _("register")
    #     verbose_name_plural = _("registers")

    # def __str__(self):
    #     return self.id

    # def get_absolute_url(self):
    #     return reverse("register_detail", kwargs={"pk": self.pk})
    


