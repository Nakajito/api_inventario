import datetime
from arrow import utcnow
from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings


SECRET_KEY = settings.SECRET_KEY

def generar_token(username):
    payload = {
        'username': username,
        'exp': utcnow + datetime.timedelta(hours=1),
        'iat': utcnow
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def validar_token(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Token es requerido'},status=status.HTTP_401_UNAUTHORIZED)
    
    token = token.replace('Bearer', '')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token expirado'}, status=status.HTTP_401_UNAUTHORIZED)
    
    except jwt.InvalidTokenError:
        return Response({'error': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)