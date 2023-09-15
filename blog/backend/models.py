from django.db import models

# class Image(models.Model):
#     title = models.CharField(max_length=255)
#     images = models.ImageField(upload_to='media/', default='10')

#     def __str__(self) -> str:
#         return self.title

class Post(models.Model):
    nomi = models.CharField(max_length=500)
    narxi = models.IntegerField()
    rasm1 = models.ImageField(upload_to='media/', default='10')
    slug = models.SlugField(null='True')
    # rasm1 = models.ImageField(upload_to='media/')



    def __str__(self) -> str:
        return self.nomi