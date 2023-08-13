from django.db import models

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    tittle = models.CharField(max_length=150)
    year = models.IntegerField()
    gender = models.CharField(max_length=150)

    def __str__(self):
        return self.tittle