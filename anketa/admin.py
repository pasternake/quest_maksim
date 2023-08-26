from django.contrib import admin
from .models import Respondent
from .models import Anketa
from .models import Question
from .models import Answer
from .models import RespondentAnswer

# Register your models here.
admin.site.register(Respondent)
admin.site.register(Anketa)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(RespondentAnswer)