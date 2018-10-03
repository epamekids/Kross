from django.db import models

class Request(models.Model):
  title = models.CharField(max_length = 70)
  text = models.TextField()
  date = models.DateTimeField()
  image = models.ImageField()

  def __str__(self):
      return self.title
      return self.image