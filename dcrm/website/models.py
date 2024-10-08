from django.db import models

class Record(models.Model):

    creation_data = models.DateTimeField(auto_now_add = True)
    
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Gamedata(models.Model):
    character_name = models.CharField(max_length = 64)
    stars = models.IntegerField()