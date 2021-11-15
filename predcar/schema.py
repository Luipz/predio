import graphene
from graphene_django import DjangoObjectType

#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual
import sys
sys.path.append("..")

from predios.models import Usuarios, Predio

class UsuariosType(DjangoObjectType):
    class Meta:
        model = Usuarios
        fields = ("id", "name", "last_name", "predios")

class PredioType(DjangoObjectType):
    class Meta:
        model = Predio
        fields = ("id", "car_brand", "license_plate", "usuarios")

class Query(graphene.ObjectType):
    all_predios = graphene.List(PredioType)
    usuarios_by_name = graphene.Field(UsuariosType, name=graphene.String(required=True))

    def resolve_all_predios(root, info):
        # We can easily optimize query count in the resolve method
        return Predio.objects.select_related("usuarios").all()

    def resolve_usuarios_by_name(root, info, name):
        try:
            return Usuarios.objects.get(name=name)
        except Usuarios.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)