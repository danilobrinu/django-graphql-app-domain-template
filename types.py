# Built-in packages

# Third-party packages
from graphene import Node, ID, String, ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from . import models, filters


class {{ camel_case_app_name }}(DjangoObjectType, interfaces=(Node,)):
    """An object with an ID."""

    class Meta:
        model = models.{{ camel_case_app_name }}
        filter_fields = []


class {{ camel_case_app_name }}OutputMutation(ObjectType):
    Output = {{ camel_case_app_name }}


class {{ camel_case_app_name }}WhereUniqueInput(InputObjectType):
    id = ID()


class {{ camel_case_app_name }}WhereInput(InputObjectType):
    pass


class {{ camel_case_app_name }}CreateInput(InputObjectType):
    pass


class {{ camel_case_app_name }}UpdateInput(InputObjectType):
    pass
