from django.db import models

class Payment(models.Model):
    aid = models.CharField(max_length=50)
    tid = models.CharField(max_length=50)
