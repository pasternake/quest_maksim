from django.db import models


# Create your models here.
class Respondent(models.Model):
    """
    Респондент для анкеты
    """

    # Fields
    last_name = models.CharField(max_length=40, help_text="Фамилия респондента")

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.last_name


class Anketa(models.Model):
    """
    Анкета
    """

    # Fields
    name = models.CharField(max_length=40, help_text="Имя(название) анкеты")
    discription = models.CharField(max_length=100, help_text="Описание анкеты")

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return 'Анкета: ' + self.name


class Question(models.Model):
    """
    Вопрос для анкеты
    """

    # Fields
    anketa = models.ForeignKey("Anketa", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, help_text="Имя(название) вопроса")

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name


class Answer(models.Model):
    """
    Варианты ответов для анкеты
    """

    # Fields
    name = models.CharField(max_length=200, help_text="Имя(название) ответов")
    question = models.ForeignKey("Question", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name


class RespondentAnswer(models.Model):
    """
    Ответы респондента на вопросы для анкеты
    """

    # Fields
    respondent = models.ForeignKey("Respondent", on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey("Answer", on_delete=models.SET_NULL, null=True)
