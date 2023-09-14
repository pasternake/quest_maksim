from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("anketa/", views.anketa, name="anketa"),
    path("questions/", views.func_questions, name="questions"),
    path("thankyou/", views.func_thankyou, name="thankyou"),
]
