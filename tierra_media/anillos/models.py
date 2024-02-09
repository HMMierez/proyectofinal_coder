from django.db import models
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True) 
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen_destacada = models.ImageField()
