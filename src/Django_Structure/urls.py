from django.urls import path

from Django_Structure import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hi/', views.hi),
]
