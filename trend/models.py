from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
   
    profile_pic = models.ImageField(upload_to = 'photos/', default='default.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    CATEGORIES2 = (
        ('Rocker looks', 'Rocker looks'),
        ('Tomboy Fashion', 'Tomboy Fashion'),
        ('Sophisticated Fashion', 'Sophisticated Fashion'),
        ('Artsy Fashion', 'Artsy Fashion'),
        ('Casual Fashion', 'Casual Fashion'),
        ('Vintage Fashion', 'Vintage Fashion'),
    )
    your_fashion_taste = models.CharField(max_length=100,choices=CATEGORIES2,default='No style')
    contact = models.CharField(max_length = 12)
    def __str__(self):
        return self.contact
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

class Product(models.Model):
    CATEGORIES = (
        ('Menswear', 'Menswear'),
        ('womenswear', 'womenswear'),
        ('Generalised', 'Generalised')
    )
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="user_name")
    profile = models.ForeignKey(Profile,null=True)
    product_name = models.CharField(max_length =30)
    gender = models.CharField(max_length =50,choices=CATEGORIES)
    CATEGORIES2 = (
        ('Rocker looks', 'Rocker looks'),
        ('Tomboy Fashion', 'Tomboy Fashion'),
        ('Sophisticated Fashion', 'Sophisticated Fashion'),
        ('Artsy Fashion', 'Artsy Fashion'),
        ('Casual Fashion', 'Casual Fashion'),
        ('Vintage Fashion', 'Vintage Fashion'),
    )
    category = models.CharField(max_length=100,choices=CATEGORIES2,default='No style')
    description = models.CharField(max_length =50)  
    post_date = models.DateTimeField(auto_now_add=True)
    
     
    def __str__(self):
        return self.product_name

    def save_prod(self):
        self.save()
    def delete_prod(self):
        self.delete()

class Comment(models.Model):
    image = models.ForeignKey('Product')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


    def save_comment(self):
        self.save()
    def delete_comment(self):
        self.delete()

class News:
    '''
    News class to define a news objects
    '''
    def __init__(self,author,title,description,urlToImage,publishedAt,content):
    
        self.author=author
        self.title=title
        self.description=description
        self.urlToImage= urlToImage
        self.publishedAt=publishedAt
        self.content=content
