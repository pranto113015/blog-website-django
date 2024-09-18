from django.db import models
# Create your models here.
class Article(models.Model):
    a_catagory = models.CharField(max_length=250)
    a_title = models.CharField(max_length=80)
    a_authorname = models.CharField(max_length=100)
    a_date = models.DateField()
    a_description = models.CharField(max_length=500)
    image= models.ImageField(upload_to='article_img/', default='#')
    
    def __str__(self):
     return self.a_title

class TrendingPost(models.Model):
    trending_title = models.CharField(max_length=80)
    trending_date = models.DateField()
    trending_image= models.ImageField(upload_to='trending_img/', default='#')
     
    def __str__(self):
     return self.trending_title

class About(models.Model):
    about_title = models.CharField(max_length=80)
    about_description = models.CharField(max_length=600)
    about_pofile_image= models.ImageField(upload_to='about_img/', default='#')
    about_cover_image= models.ImageField(upload_to='about_img/', default='#')

    def __str__(self):
        return self.about_title


# this is for customer feedback form
class Contact(models.Model):
   name = models.CharField(max_length=200)
   email = models.EmailField()
   message = models.CharField(max_length=1000) 
    
   def __str__(self):
    return self.name
