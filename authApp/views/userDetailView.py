from rest_framework import generics
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # ESTE GET NO ES NECESARIO, YA AL HEREDAR DE GENERICS, DJANGO SUPONE QUE SE VA A USAR EL GET. si lo ponemos sirve y si no lo ponemos tambien funciona.
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


# YA NO TENEMOS QUE VERIFICAR EL TOKEN, DE ESO SE ENCARGARA EL API GATEWAY

# agrego otra opciones para completar CRUD por si hacemos las funcionalidades de usuario mas completas

class UserUpdateView(generics.UpdateAPIView):  # Para actualizar un usuario.
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):

        # partial_update , actualiza uno o varios elementos del enfermero, no necesariamente tiene que ser todo
        return super().partial_update(request, *args, **kwargs)


# Para poder eliminar un usuario.
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    seializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)
