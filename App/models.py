from django.db import models
from froala_editor.fields import FroalaField

class Hashing(models.Model):
    title = models.CharField(max_length=150, blank=True)
    hash_name = models.CharField(max_length=256)
    description = FroalaField()

    def __str__(self):
        return self.hash_name
