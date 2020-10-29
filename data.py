# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models, types, serializers


def get_{{ app_name }}(where: types.{{ camel_case_app_name }}WhereUniqueInput) -> models.{{ camel_case_app_name }}:
    _, instance_id = from_global_id(where.get("id"))
    instance = models.{{ camel_case_app_name }}.objects.get(id=instance_id)
    
    return instance


def create_{{ app_name  }}(data: types.{{ camel_case_app_name }}CreateInput) -> models.{{ camel_case_app_name }}:
    serializer = serializers.{{ camel_case_app_name }}Serializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def update_{{ app_name }}(where: types.{{ camel_case_app_name }}WhereInput, data: types.{{ camel_case_app_name }}UpdateInput) -> models.{{ camel_case_app_name }}:
    instance = get_{{ app_name }}(where)
    serializer = serializers.{{ camel_case_app_name }}Serializer(instance, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_{{ app_name }}(where: types.{{ camel_case_app_name }}WhereUniqueInput) -> models.{{ camel_case_app_name }}:
    instance = get_{{ app_name }}(where)
    instance.delete()

    return instance