from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #si el usuario es eliminado, el perfil tambien se elimina, con el cascade
    image = models.ImageField(default='default.jpg', upload_to= 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # despues de crear esto hago migraciones





# Create your models here.
