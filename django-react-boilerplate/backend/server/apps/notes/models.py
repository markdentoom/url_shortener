from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    short_url = models.TextField(blank=True)
    request_count = models.IntegerField(default=1)
