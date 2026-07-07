from django.db import models

# Create your models here.
class Board(models.Model):
    board_number = models.IntegerField()
    category = models.CharField(max_length=20)
    clue = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    value = models.IntegerField()
    staus = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.category} - {self.clue} - {self.response} - {self.value}"