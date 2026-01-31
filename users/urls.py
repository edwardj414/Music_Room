from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('delete-user/', DeleteUser.as_view(), name='delete-user'),
]