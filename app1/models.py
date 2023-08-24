from django.db import models

# Create your models here.
class Userregister(models.Model):
    name =models.CharField(max_length=200)
    email =models.EmailField()
    number =models.IntegerField()
    address =models.TextField()
    password =models.CharField(max_length=12)
    # def _str_(self):
    #   retrun str(self.name)+" "+str(self.email)

class Category(models.Model):
        Categoryname=models.CharField(max_length=200)
        def _str_(self):
              return self.Categoryname
        
class product(models.Model):
      Category=models.ForeignKey(Category,on_delete=models.CASCADE)
      name=models.CharField(max_length=200)
      price=models.IntegerField()
      discription=models.TextField()


       
    
