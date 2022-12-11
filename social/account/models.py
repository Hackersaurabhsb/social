from django.db import models
from django.conf import settings
#the current model is for views login view
# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #The one-to-one field user will be used to associate profiles with users. With on_delete=models.CASCADE, 
    #we force the deletion of the related Profile object when a User object gets deleted.
    date_of_birth=models.DateTimeField(blank=True,null=True)
    photo=models.ImageField(upload_to='users/%y/%m/%d/',blank=True)
    def __str__(self):
        return f'Profile of {self.user.username}'


#In order to keep your code generic, use the get_user_model() method to retrieve the user 
#model and the AUTH_USER_MODEL setting to refer to it when defining a model’s relationship 
#with the user model, instead of referring to the auth user model directly.