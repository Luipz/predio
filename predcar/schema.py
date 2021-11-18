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
        fields = ("id", "car_brand", "license_plate")

class Query(graphene.ObjectType):
    all_predios = graphene.List(PredioType)
    usuarios_by_name = graphene.Field(UsuariosType, name=graphene.String(required=True))

    def resolve_all_predios(root, info):
        # We can easily optimize query count in the resolve method
        return Predio.objects.all()

    def resolve_usuarios_by_name(root, info, name):
        try:
            return Usuarios.objects.get(name=name)
        except Usuarios.DoesNotExist:
            return None
    
class PredioMutation(graphene.Mutation):
    class Arguments:
        carBrand = graphene.String(required=True)
        licensePlate = graphene.String(required=True)
    predio = graphene.Field(PredioType)

    @classmethod
    def mutate(cls, root, info, carBrand, licensePlate):
        predio = Predio(car_brand = carBrand, license_plate = licensePlate)
        predio.save()
        return PredioMutation(predio = predio)

class Mutation(graphene.ObjectType):
    add_predio = PredioMutation.Field()

schema = graphene.Schema(query=Query, mutation= Mutation)