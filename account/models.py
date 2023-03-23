from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=180)

    def get_name(self):
        return self.name