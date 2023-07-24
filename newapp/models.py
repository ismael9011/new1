from django.db import models

# Properties model - currently to include property name and picture. Model migrated, and no entries are there yet as of 2023-07-20 3:13 PM    
class Properties(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='property_images/')
    #currently adding address field in
    address = models.CharField(max_length=200, default= 'address_filler')
    #housing selection for the property type field
    hchoices = (
    ('a', 'Condo'),
    ('b', 'House'),
    )
    type = models.CharField(max_length=1, choices=hchoices, default= 'a')
    distance = models.DecimalField(decimal_places= 2, max_digits= 5, default=1.00) 
    
# Review models
class Review(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=1) 
    pub_date = models.DateTimeField('date posted')
    text = models.CharField(max_length=200, default= 'text_filler')
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, null=True, default=None)