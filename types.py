# Built-in packages

# Third-party packages
import graphene as gql
import graphene_django as django_gql

# Local packages
from . import models


class {{ camel_case_app_name }}(django_gql.DjangoObjectType, interfaces=(gql.Node,)):
    """An object with an ID."""

    class Meta:
        model = models.{{ camel_case_app_name }}
        filter_fields = []


class {{ camel_case_app_name }}OutputMutation(gql.ObjectType):
    Output = {{ camel_case_app_name }}


class {{ camel_case_app_name }}WhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class {{ camel_case_app_name }}WhereInput(gql.InputObjectType):
    pass


class {{ camel_case_app_name }}CreateInput(gql.InputObjectType):
    pass


class {{ camel_case_app_name }}UpdateInput(gql.InputObjectType):
    pass
