from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class Link(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    url = models.URLField(_("URL Link"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    clicks = models.PositiveIntegerField(_("Clicks"), default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks}"
    
    def click(self):
        self.clicks +=1
        self.save()
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        return super().save(*args, **kwargs)
            
