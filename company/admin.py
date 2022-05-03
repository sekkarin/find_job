from django.contrib import admin
from company.models import Type_job ,Job ,Company , Job_application
# Register your models here.
admin.site.register(Type_job)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Job_application)