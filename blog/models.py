from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    fecha= models.DateTimeField(auto_now_add=True) #auto_now_add lo que hace es tomar la hora en la que fue creado el objeto y registrarlo
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #con foreignkey relaciono el usuario con el post. El argumento on_delete se usa para determinar que quiero hacer al borrar el usuario. En este caso, con CASCADE se esta determinando que cuando un usuario es eliminado, todos sus posts tambien se eliminan.

    def __str__(self):
        return self.title














