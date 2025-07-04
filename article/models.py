from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
