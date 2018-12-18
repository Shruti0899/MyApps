from django.db import models

#database
# Create your models here.
class Form(models.Model):  #import it in admin.py for viewing it
    name= models.CharField(max_length = 10);
    psw = models.CharField(max_length = 10);

    #if table modified then "makemigrations"
    #then "migrate"

class Regform(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    phno = models.CharField(max_length=10)
    psw = models.CharField(max_length=10)

class Userform(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    psw=models.CharField(max_length=10)
    

