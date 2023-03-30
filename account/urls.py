from django.urls import path
from account.views import *

urlpatterns = [
    path('sign_up', sign_up),
    path('log_in', log_in)
]