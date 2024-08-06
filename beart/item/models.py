from django.db import models
from django.contrib.auth.models import User
import logging

logging.basicConfig(level = logging.INFO)

logger = logging.getLogger('django')
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    Category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank =True, null= True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images')
    id_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)

    def delete(self):
        logger.info("delete called")
        if self.image:
            self.image.delete(save=False)
            logger.info("image removed from s3")
        # Call the superclass delete method
        super(Item, self).delete()

    def __str__(self):
        return self.name