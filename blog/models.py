from django.db import models
from django.utils import timezone

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types 
class Post(models.Model):
    #integer = models.IntegerField(default=34)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title