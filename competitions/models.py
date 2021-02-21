from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Competition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='')
    time = models.DateTimeField(null=True,blank=True)
    image = models.ImageField(upload_to="images",default="default-image.png",blank=True,null=True)
    description = models.TextField(max_length=500, default='')
    venue = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    seats = models.IntegerField(default=50,null=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    class Meta:
        ordering = ["time"]
        verbose_name_plural = 'competitions'
        
    def add_user_to_list_of_attendees(self, user):
        registration = CompetitionRegistration.objects.create(user = user,
                                                    competition = self)

    def decrement_seats(self):
        self.seats -= 1
        self.save()

class CompetitionRegistration(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Attendes for competitions'
        unique_together = ('competition','user')
    
