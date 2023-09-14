from django.shortcuts import render

from anketa.models import Anketa, Answer, Question, Respondent

# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_anketa = Anketa.objects.all().count()
    num_question = Question.objects.all().count()
    num_answer = Answer.objects.all().count()
    num_respondent = Respondent.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        "index.html",
        context={
            "num_anketa": num_anketa,
            "num_question": num_question,
            "num_answer": num_answer,
            "num_respondent": num_respondent,
        },
    )


def anketa(request):
    return render(
        request,
        "anketa.html",
        context={},
    )
