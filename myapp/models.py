from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    book_image = models.ImageField(default='default.jpg', upload_to='book_images/')

    def __str__(self):
        return self.name


