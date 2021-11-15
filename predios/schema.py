import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from predios.models import Usuarios, Predio


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class UsuariosNode(DjangoObjectType):
    class Meta:
        model = Usuarios
        filter_fields = ['name', 'last_name','predios']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class PredioNode(DjangoObjectType):
    class Meta:
        model = Predio
        # Permite un filtrado mas avanzado
        filter_fields = {
            'car_brand': ['exact', 'icontains', 'istartswith'],
            'license_plate': ['exact', 'icontains'],
            'usuarios': ['exact'],
            'usuarios__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    usuarios = relay.Node.Field(UsuariosNode)
    all_usuaries = DjangoFilterConnectionField(UsuariosNode)

    predio = relay.Node.Field(PredioNode)
    all_predioes = DjangoFilterConnectionField(PredioNode)


