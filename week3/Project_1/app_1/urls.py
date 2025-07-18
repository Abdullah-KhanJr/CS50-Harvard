from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("abdullah", views.abdullah, name="abdullah"),
    path("david1", views.another_function, name = "david"),
    path("<str:name>/<str:gender>/<int:age>", views.greet, name="greetings")
]
