from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
import os

# Create your models here.
class Faq(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False)
    answer = RichTextField()

class SingletonModel(models.Model):
    class Meta:
        abstract = True  # Ensure this is an abstract model

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Return the last created instance, or None if no instance exists
        try:
            return cls.objects.latest('id')  # Fetch the latest by ID
        except cls.DoesNotExist:
            return None  # Return None if no instance exists
    
class Landing(SingletonModel):
    video = models.FileField(upload_to='landing_video/')  # Specify the folder for videos

    def __str__(self):
        return "Landing Video"
    
    def save(self, *args, **kwargs):
        # Check if video has already been saved before re-saving
        if self.pk:  # Only run this if the object already exists
            original = Landing.objects.get(pk=self.pk)
            if original.video != self.video:
                # Handle case when video is changed
                original.video.delete(save=False)

        super(Landing, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the video file when the model instance is deleted
        if self.video:
            if os.path.isfile(self.video.path):
                os.remove(self.video.path)
        super(Landing, self).delete(*args, **kwargs)

@receiver(post_delete, sender=Landing)
def delete_video_file(sender, instance, **kwargs):
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)