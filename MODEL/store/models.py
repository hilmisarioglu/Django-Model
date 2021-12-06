from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=50, blank=True, null=True , default= 'Ürün ...' ) 
    sayi = models.IntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        print('girilen sayinin iki kati' + ' ' +str(self.sayi * 2))
        self.name = self.name + ' Eklendi '
        self.sayi = self.sayi* 2
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(f'{self.name}')
    
    class Meta :
        verbose_name_plural = 'Ürünler'
    
    
        
    
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=360)
#     image=models.ImageField(
#         upload_to='posts/img/',
#         validators=[validate_ext],
#         blank=True,
#         null=True
#     )
#     liked = models.ManyToManyField(
#         Profile,
#         default=None,
#         blank=True,
#         related_name='liked',
#     )
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTime(auto_now_add=True)
#     author = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE,
#         related_name='author'
#     )
#     def num_likes(self):
#         return self.liked.all().count()
#     def __str__(self):
#         return str(self.title)
#     def get_absolute_url(self):
#         return reverse('posts:gp-details' , kwargs={'pk':self.pk})
#     class Meta:
#         ordering=('-created',)