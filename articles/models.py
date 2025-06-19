from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title