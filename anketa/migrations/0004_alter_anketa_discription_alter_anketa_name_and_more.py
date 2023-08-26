# Generated by Django 4.2.3 on 2023-08-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketa', '0003_answer_alter_anketa_name_respondentanswer_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anketa',
            name='discription',
            field=models.CharField(help_text='Описание анкеты', max_length=100),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='name',
            field=models.CharField(help_text='Имя(название) анкеты', max_length=40),
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(help_text='Имя(название) ответов', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(help_text='Имя(название) вопроса', max_length=200),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='last_name',
            field=models.CharField(help_text='Фамилия респондента', max_length=40),
        ),
    ]
