from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
class CovidResource(models.Model):
    resource_type=models.CharField(max_length=100)
    state=models.CharField(max_length=256)
    city=models.CharField(max_length=50)
    title=models.CharField(max_length=256)
    description=models.TextField(max_length=2000)
    tags=models.CharField(max_length=500,blank=True,null=True)
    date_added=models.DateTimeField(blank=True,null=True)
    image1=models.ImageField( upload_to='images', blank=True,null=True)
    image2=models.ImageField( upload_to='images', blank=True,null=True)
    image3=models.ImageField( upload_to='images', blank=True,null=True)
    def save(self, *args, **kwargs): 
        self.date_added = datetime.now()
        super(CovidResource, self).save(*args, **kwargs)
    @property
    def image1URL(self):
        try:
            url= self.image1.url
        except:
            url=None
        return url
    @property
    def image2URL(self):
        try:
            url= self.image2.url
        except:
            url=None
        return url
    @property
    def image3URL(self):
        try:
            url= self.image3.url
        except:
            url=None
        return url
