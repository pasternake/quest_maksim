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
    anketa_list = Anketa.objects.all()

    results = []
    for item in anketa_list:
        print(item.name)
        results.append({"name": item.name, "description": item.discription})

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
            "results": results,
        },
    )


def anketa(request):
    return render(
        request,
        "anketa.html",
        context={},
    )


def func_thankyou(request):
    return render(
        request,
        "thankyou.html",
        context={},
    )


def func_questions1(request):
    return render(
        request,
        "question1.html",
        context={},
    )


def func_questions2(request):
    return render(
        request,
        "question2.html",
        context={},
    )


def func_questions3(request):
    return render(
        request,
        "question3.html",
        context={},
    )
