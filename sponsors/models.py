from django.db import models
from django.utils.text import slugify
# Create your models here.

class SponsorType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    type = models.ForeignKey(SponsorType, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to="images",default="default-image.png",blank=True,null=True)
    slug = models.SlugField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name_plural = 'sponsors'
        


    


