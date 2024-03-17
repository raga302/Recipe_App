from django.db import models

# Create your models here.
class Signup_Db(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    password = models.TextField(null=True)
    

class Admin_Panel_Db(models.Model):
    login_or_signup_email = models.EmailField(null=True)
    recipe_name = models.CharField(max_length=50, null=True)
    recipe_dscription = models.TextField(null=True)
    recipe_image = models.ImageField(null=True)
