from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,help_text='Название статьи',default='Автор долбоеб')
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    text=models.TextField(max_length=500,default="Автор долбоеб")
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fil=models.FileField(upload_to='documents/',null=True)
    date=models.DateField(auto_now=True)
    STATUS_VAR=(
        ('В теории','В теории'),
        ('В проекте','Проектирование'),
        ('Альфа','Альфа'),
        ('Бета','Бета'),
        ('Релиз','Релиз')
    )
    status=models.CharField(max_length=10,choices=STATUS_VAR,blank=True,default='t')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id',]
    