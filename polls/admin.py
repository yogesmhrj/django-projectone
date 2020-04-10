from django.contrib import admin

from polls.model.questions.question_category import QuestionCategory
from polls.model.questions.questions import Question

admin.site.register(QuestionCategory)
admin.site.register(Question)
