from django.db import models


class News(models.Model):
  title = models.CharField(max_length=200)
  link = models.URLField(max_length=200)
  description = models.TextField()
  published_date = models.CharField(max_length=50)

  def __str__(self):
    return self.title






