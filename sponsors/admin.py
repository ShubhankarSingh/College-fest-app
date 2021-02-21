from django.contrib import admin

from .models import Sponsor, SponsorType
# Register your models here.

admin.site.register(Sponsor)
admin.site.register(SponsorType)