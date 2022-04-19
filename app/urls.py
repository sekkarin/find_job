from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name='login'),
    path('login/register/',views.register,name='register'),
    path('logout/',views.logout,name="logout"),
    path('job/<int:id>/',views.job,name="job"),
    path("upload/", views.upload_file, name="uploadfile"),
]
