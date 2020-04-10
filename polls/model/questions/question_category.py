from django.db import models

class QuestionCategory(models.Model):
    category_text = models.CharField(max_length=255)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.category_text