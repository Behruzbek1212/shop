from django.db import models


class Post(models.Model):
    asosiy_rasm = models.ImageField(upload_to='media/', default='10')
    nomi = models.CharField(max_length=500)
    hozirgi_narx = models.IntegerField()
    oldingi_narx = models.IntegerField()
    sotuvda_nechta = models.IntegerField()
    tavsif = models.TextField()
    
    
    
   
    slug = models.SlugField(null='True')

    def __str__(self) -> str:
        return self.nomi
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    rasmlar = models.ImageField(upload_to='media/')
    
    def __str__(self) -> str:
        return self.post.nomi