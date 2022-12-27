from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=150)

    def __str__(self):
        return self.title
