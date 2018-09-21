from django.db import models
from django.conf import settings
import uuid


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    created = models.DateField(auto_now=True)
    content = models.TextField()


# Create your models here.
