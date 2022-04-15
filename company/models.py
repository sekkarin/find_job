from django.db import models

# Create your models here.

class Type_job (models.Model):
    id_type = models.BigAutoField(primary_key=True)
    name_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_type
    
class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_job =  models.CharField(max_length=100)
    data_post =  models.DateTimeField(auto_now=False)
    job_title = models.IntegerField()
    detial = models.CharField(max_length=100)
    property_job = models.CharField(max_length=50)
    job_application = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    id_type = models.ForeignKey(Type_job, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_job
    
class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_company = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    discripts = models.CharField(max_length=300)
    welfare  = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    id_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_company
    


