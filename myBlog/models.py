from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Here the url pattern is defined using '/%s'/ where %s is the placeholder for the slug 
        # We are not using rever() function which will ftech the url pattern from urls.py using the url pattern name 
        return '/%s/' % self.slug
    

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    ARCHIVE = 'archive'
    
    CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft'),
    (ARCHIVE, 'Archive'),
    )
    
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content= HTMLField()
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=DRAFT)
    views = models.IntegerField(default = 0)
    # categories = models.ManyToManyField(Category)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse( "myBlog:category_list", self.category.slug)
    
class Comments(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    