from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name='login'),
    path('login/register/',views.register,name='register'),
    path('cookie/test/',views.cookie_test,name="cookie_test"),
    path('cookie/test/result/',views.cookie_test_result,name="cookie_test_result"),
    path('logout/',views.logout,name="logout"),
    path('job/<int:id>/',views.job,name="job"),
]
