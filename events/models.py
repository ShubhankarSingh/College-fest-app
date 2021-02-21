from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, unique=True)
    time = models.DateTimeField(null=False)
    image = models.ImageField(upload_to="images",default="default-image.png",null=True)
    description = models.TextField(max_length=500,null=False)
    slug = models.SlugField(max_length=200)
    is_online = models.BooleanField(default=False)
    meet_link = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    class Meta:
        ordering = ["time"]
        verbose_name_plural = 'events'
        
    def add_user_to_list_of_attendees(self, user):
        registration = EventRegistration.objects.create(user = user,
                                                    event = self)

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Attendes for events'
        unique_together = ('event','user')
    
