# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models, types, serializers


def get_{{ camel_case_app_name }}(where: types.{{ app_name }}WhereUniqueInput) -> models.{{ app_name }}:
     _, instance_id = from_global_id(where.get("id"))
    instance = models.{{ app_name }}.objects.get(id=instance_id)
    
    return instance


def create_{{ camel_case_app_name  }}(data: types.{{ app_name }}CreateInput) -> models.{{ app_name }}:
    serializer = serializer.{{ app_name }}Serializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def update_{{ camel_case_app_name }}(where: types.{{ app_name }}WhereInput, data: types.{{ app_name }}UpdateInput) -> models.{{ app_name }}:
    instance = get_{{ camel_case_app_name }}(where)
    serializer = serializers.{{ app_name }}Serializer(instance, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_{{ camel_case_app_name }}(where: types.{{ app_name }}WhereUniqueInput) -> models.{{ app_name }}:
    instance = get_{{ camel_case_app_name }}(where)
    instance.delete()

    return instance