from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("anketa/", views.anketa, name="anketa"),
    path("thankyou/", views.func_thankyou, name="thankyou"),
    path("questions1/", views.func_questions1, name="questions1"),
    path("questions2/", views.func_questions2, name="questions2"),
    path("questions3/", views.func_questions3, name="questions3"),
]
