from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,help_text='Название статьи',default='Автор долбоеб')
    image=models.ImageField(upload_to='images',default='image not found')
    text=models.TextField(max_length=1000,default='Автор долбоеб')
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id',]


