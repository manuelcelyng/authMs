"""Esta view se usa para tener verificacion de toquen desde la API GATEWAY por eso no se implementa en las otras view, el manejo de token se hace desde API GATEWAY +++++!!Importante!!*++++++"""

from django.conf import settings  # Para traer el algotirmo de codificacion
from rest_framework import status  # codigos que podemos dar de respuesta
# restornar la informacion en JSON, tiene que ser lista o diccionario
from rest_framework.response import Response
# funcionalidades del token
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
# Manejo de errores de token , Excepctions
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# serializador de token para validar el token, ESTO lo trae hecho la libreria.
from rest_framework_simplejwt.serializers import TokenVerifySerializer


class VerifyTokenView(TokenVerifyView):  # View para validacion de toquen

    def post(self, request, *args, **kwargs):  # SE ENVIA EL TOQUEN QUE SE VA A VERIFICAR en un BODY
        # LA DATA RECIBIDA LA GUARDAMOS EN EL SERIALIZER
        serializer = TokenVerifySerializer(data=request.data)
        # generamos el algoritmo para procesar el token, este algoritmo lo traemos del settings.py DEFINIDO EN EL PROYECTO
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])

        try:
            # verificar que la informacion que llego en el cuerpo, quede bien guardada en el serializer
            serializer.is_valid(raise_exception=True)
            # ejecuta el tokenBackend y decodifica la informacion que nos está llegando. el token
            token_data = tokenBackend.decode(
                request.data['token'], verify=False)
            # guardamos el id verificado del usuario
            serializer.validated_data['UserId'] = token_data['user_id']

        except TokenError as e:  # lanzar error en caso de falla el token
            raise InvalidToken(e.args[0])

        # Respuesta del token validado en caso de estár correcto, devuelve un JSON
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
