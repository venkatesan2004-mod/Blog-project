from django.db import models
from django.utils.text import slugify




class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
       return self.name    
    
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(max_length=255)
    img_url=models.URLField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True , unique=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
       self.slug=slugify(self.title)
       super().save(*args,**kwargs)

    def __str__(self):
      return self.title  
    
def __str__(self):
    return self.stdout.write(self.style.SUCCESS("Completed migration"))  


class AboutUS(models.Model):
   content=models.TextField()

class chatbot(models.Model):
   Query=models.TextField()
   Response=models.TextField()