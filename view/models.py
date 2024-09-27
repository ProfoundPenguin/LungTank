from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)