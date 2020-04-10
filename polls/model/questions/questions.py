import datetime
from django.db import models
from polls.model.questions.question_category import QuestionCategory

class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, null=True, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text