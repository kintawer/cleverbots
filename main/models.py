from django.db import models

# Create your models here.


class Image(models.Model):
    content = models.ImageField(verbose_name='Изображение', upload_to='images/')
    place = models.CharField(verbose_name='Место', max_length=55)
    create_date = models.DateField(verbose_name='Дата создания', auto_now=True, editable=False)
