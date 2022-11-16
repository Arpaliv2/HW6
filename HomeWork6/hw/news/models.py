from django.db import models

# Create your models here.
class News(models.Model):
    time_of_addition = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'{self.heading.title()}\n{self.text[:20]}\n'