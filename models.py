from distutils.command.upload import upload
import email
from unicodedata import category, name
from django.db import models
from django.utils.html import escape


class product(models.Model) :
    product_id= models.AutoField
    product_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50,default="")
    sub_catagory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    desc = models.TextField(max_length=300)
    pub_date= models.DateField()
    product_image = models.ImageField(upload_to = 'shop/image', default="")
    

    def __str__(self) :
        return self.product_name

class basic_image(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='shop/image',default='')

    def __str__(self) -> str:
        return self.name
    
        

class query(models.Model) :
    id= models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField(max_length=300)

    def __str__(self) :
        return self.name
    
class sign_in(models.Model) :
    id= models.AutoField
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class cart(models.Model):
    image=models.ImageField(upload_to = 'shop/image', default="")
    category=models.CharField(max_length=50,default='')
    name=models.CharField(max_length=50,default='')
    price=models.IntegerField(default=0)
    qty=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    

    