from django.db import models

# Create your models here.

class Feed(models.Model): 
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    city = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"