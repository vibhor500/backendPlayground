from django.db import models

class Text(models.Model):
    hlloworld = models.CharField(max_length=100)

    def __str__(self):
        return self.str
