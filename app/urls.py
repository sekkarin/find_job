from django.urls import path
from . import views
from app.views import   JobGroup , MyWork
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name='login'),
    path('login/register/',views.register,name='register'),
    path('logout/',views.logout,name="logout"),
    path('job/<int:id>/',views.job,name="job"),
    path("upload/", views.simple_upload, name="uploadfile"),
    path("job_group/<int:id>/", JobGroup.as_view(), name="groupjob"),
    path("my_works/<int:id>/",MyWork.as_view(),name='mywork'),
    path('like_job/<int:id_user>/<int:id_job>/',views.like_job,name="likejob"),
]
