from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import *

urlpatterns = [
    # path('sign_up', sign_up),
    # path('log_in', log_in)
    path('register/', register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/profile/', profile, name='profile'),
]
