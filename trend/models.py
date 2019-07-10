from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
   
    profile_pic = models.ImageField(upload_to = 'photos/', default='default.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

class Product(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="user_name")
    profile = models.ForeignKey(Profile,null=True)
    product_name = models.CharField(max_length =30)
    category = models.CharField(max_length =50,choices=((1,'Menswear'),(2,'Womenswear')))
    description = models.CharField(max_length =50)
    post_date = models.DateTimeField(auto_now_add=True)
    
     
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    def delete_image(self):
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