from django.db import models

# Create your models here.


class Todo(models.Model):

    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=255, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title