from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Faq(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False)
    answer = RichTextField()