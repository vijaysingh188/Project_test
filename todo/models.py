from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title