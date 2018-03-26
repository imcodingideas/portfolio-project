from django.db import models

class Blog(models.Model):
  image = models.ImageField(upload_to='images/')
  title = models.CharField(max_length=75)
  pub_date = models.DateTimeField()
  body = models.TextField()