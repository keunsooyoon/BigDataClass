from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

    created_at = models.DateTimeField()
    # author은 나중에


    def __str__(self):
        return f'[{self.pk}]{self.title}'