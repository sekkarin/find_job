from django.db import models

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
    image = models.URLField(max_length=200)
    # id_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    # id_job = models.IntegerField(default=0)
    def __str__(self):
        return self.name_company
class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_job =  models.CharField(max_length=100)
    data_post =  models.DateTimeField(auto_now=False)
    job_title = models.IntegerField()
    detial = models.CharField(max_length=100)
    property_job = models.CharField(max_length=50)
    job_application = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    salary = models.FloatField(default=0)
    id_type = models.ForeignKey(Type_job, on_delete=models.CASCADE)
    id_company  = models.ForeignKey(Company, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name_job

    


