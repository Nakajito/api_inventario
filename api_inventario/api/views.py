from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .token_utils import validar_token
from rest_framework_simplejwt.tokens import RefreshToken
from .services import obtener_usuarios, obtener_productos, obtener_categorias
from django.contrib.auth.hashers import make_password
from .models import Usuarios, Producto, Categoria


@api_view(['POST'])
def obtener_token(request):
    username = request.data.get('username')
    password =request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Usuario y contraseña son requeridos'}, status=400)
    
    try:
        usuario = Usuarios.objects.get(username=username)
        if (password == usuario.password_hash):
            refresh = RefreshToken.for_user(usuario)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
                })
        else:
            return Response({'error': 'Usuario o contraseña incorrectos'}, status=400)
    
    except Usuarios.DoesNotExist:
        return Response({'error': 'El usuario no existe'}, status=400)