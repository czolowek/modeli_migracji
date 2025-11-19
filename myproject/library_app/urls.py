from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("students/", views.students, name="students"),
    path("take/", views.take_book, name="take_book"),
]
