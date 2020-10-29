# Built-in packages

# Third-party packages
from graphene import Node, ID, String, ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from . import models, filters


class {{ app_name }}(DjangoObjectType, interfaces=(Node,)):
    """An object with an ID."""

    class Meta:
        model = models.{{ app_name }}
        filter_fields = []


class {{ app_name }}OutputMutation(ObjectType):
    Output = {{ app_name }}


class {{ app_name }}WhereUniqueInput(InputObjectType):
    id = ID()


class {{ app_name }}WhereInput(InputObjectType):
    pass


class {{ app_name }}CreateInput(InputObjectType):
    pass


class {{ app_name }}UpdateInput(InputObjectType):
    pass
