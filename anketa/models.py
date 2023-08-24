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
    name = models.CharField(max_length=20, help_text="Имя(название) анкеты")
    discription = models.CharField(max_length=20, help_text="Описание анкеты")

    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

class Vopros(models.Model):
    """
    Вопрос для анкеты
    """

    # Fields
    questionnaire_id = models.CharField(max_length=20, help_text="id Анкеты")
    name = models.CharField(max_length=20, help_text="Имя(название) вопроса")

class Variant_Otveta(models.Model):
    """
    Варианты ответов для анкеты
    """

    # Fields
    name = models.CharField(max_length=20, help_text="Имя(название) ответов")
    question_id = models.CharField(max_length=20, help_text="id вопроса")

class Otvet_na_vopros(models.Model):
    """
    Ответы на вопросы для анкеты
    """

    # Fields
    answer_id = models.CharField(max_length=20, help_text="id ответа")
    respondent_id = models.CharField(max_length=20, help_text="id респондента") 