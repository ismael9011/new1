from django.db import models

# Review models
class Review(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=1) 
    pub_date = models.DateTimeField('date posted')
    text = models.CharField(max_length=200, default= 'text_filler')
 
# Properties model - currently to include property name and picture. Model migrated, and no entries are there yet as of 2023-07-20 3:13 PM    
class Properties(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='property_images/')