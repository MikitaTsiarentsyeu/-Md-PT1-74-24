from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)


class Post(models.Model):

    POST_TYPES = [('c', "copyright"), ('a', "ad")]

    title = models.CharField(max_length=100)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
