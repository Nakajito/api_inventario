from django.db import models

class Usuarios(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'usuarios'
        
    def __str__(self):
        return self.username
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'categoria'
        
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cantidad_disponible = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'producto'
        
    def __str__(self):
        return self.nombre