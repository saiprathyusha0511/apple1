from django.urls import path
from apple1 import views
urlpatterns=[
   path('d/',views.demo),
   path('reg/',views.reg),
]