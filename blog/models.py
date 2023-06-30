from django.db import models

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)

    class Meta:
        db_table = "posts"
        get_latest_by = ["-created_at"]