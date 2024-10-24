from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length=300)  
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description