from django.urls import path
app_name='app2'
from app2 import views

urlpatterns=[
    path('h3/',views.hello,name='r3'),
]