from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    file = models.FileField(upload_to='projects/')
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title