from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import datetime
from django.utils import timezone
# Create your models here.
from django.db import models


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Category(models.Model):
    
    category = models.CharField(max_length =20)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    
    def __str__(self):
        return self.category

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category)
    blog_image = models.ImageField(upload_to = 'blog/')
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        
    def save_post(self):
        self.save()
        
    @classmethod
    def search_by_category(cls,search_term):
        categories = cls.objects.filter(category__category__icontains=search_term)
        return categories

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.objects.all()
        return blogs



