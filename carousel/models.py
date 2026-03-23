from django.db import models 
 
class CarouselImage(models.Model): 
    title = models.CharField(max_length=100, blank=True) 
    image = models.ImageField(upload_to='carousel_images/') 
    created_at = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return self.title if self.title else "Carousel Image"