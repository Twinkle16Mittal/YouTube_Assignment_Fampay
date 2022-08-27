from django.db import models

# Create your models here.
class Youtube_details(models.Model):
    __tablename__ ='youtube_details'
    title =  models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    publishing_date_time =  models.DateTimeField()
    thumbnails_urls =  models.CharField(max_length=255)
    