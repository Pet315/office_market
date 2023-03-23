from django.urls import path
from main.views import *

urlpatterns = [
    path('', main),
    # path('<int:number>/', post_number),
    # path('<int:number>/<int:month>/', post_number_month)
]