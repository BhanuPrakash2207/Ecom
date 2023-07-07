from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_description=models.CharField(max_length=400)
    published_date=models.DateField()
    category=models.CharField(max_length=70,default="")
    sub_category=models.CharField(max_length=70,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/Images",default="")
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    Problem_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(null=False,blank=False)
    phone=models.CharField(max_length=10)
    desc=models.CharField(max_length=500)

class Orders(models.Model):
    ord_id=models.AutoField(primary_key=True)
    item_JSON=models.CharField(max_length=500)
    name=models.CharField(max_length=60)
    email=models.EmailField(null=False,blank=False)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin_code=models.CharField(max_length=10)
    phone=models.CharField(max_length=20)

class order_update(models.Model):
    update_id=models.AutoField(primary_key=True)
    ord_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500)
    timestamp=models.DateField(auto_now_add=True)

