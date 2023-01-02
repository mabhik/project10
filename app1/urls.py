from django.urls import path
from app1.views import *

app_name='hello'

urlpatterns=[
    path('one1/',one1,name='one1'),
    path('one2/',one2,name='one2')
]