from django.db import models

# Create your models here.
class Moshina(models.Model):
    name = models.CharField(max_length=31)
    foto = models.CharField(max_length=356)
    content = models.TextField()
    tanlov = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class SO(models.Model):
    name = models.CharField(max_length=31)
    rasm = models.CharField(max_length=255)
    about = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rasm