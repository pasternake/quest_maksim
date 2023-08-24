from django.db import models

# Create your models here.
class Respondent(models.Model):
    """
    Респондент для анкеты
    """

    # Fields
    last_name = models.CharField(max_length=20, help_text="Фамилия респондента")

class Anketa(models.Model):
    """
    Анкета
    """

    # Fields
    name = models.CharField(max_length=20, help_text="Имя анкеты")
    discription = models.CharField(max_length=20, help_text="Описание анкеты")