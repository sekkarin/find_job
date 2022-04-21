from django.contrib import admin
from app.models import Like_job  , My_work
# from app.models import User
# # Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(User)

admin.site.register(My_work)
admin.site.register(Like_job)
