# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import Field, List, NonNull, ObjectType, Mutation, ResolveInfo

# Local packages
from . import models, types, filters, data


class Create{{ camel_case_app_name }}(types.{{ camel_case_app_name }}OutputMutation, Mutation):
    class Arguments:
        data = types.DroidCreateInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ camel_case_app_name }}, _info: ResolveInfo, data: types.DroidCreateInput,
    ) -> models.{{ camel_case_app_name }}:
        return data.create_{{ app_name }}(data)


class Update{{ camel_case_app_name }}(types.{{ camel_case_app_name }}OutputMutation, Mutation):
    class Arguments:
        where = types.{{ camel_case_app_name }}WhereUniqueInput(required=True)
        data = types.DroidUpdateInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ camel_case_app_name }}, _info: ResolveInfo, where: types.{{ camel_case_app_name }}WhereUniqueInput, data: types.DroidUpdateInput,
    ) -> models.{{ camel_case_app_name }}:
        return data.update_{{ app_name }}(where, data)


class Delete{{ camel_case_app_name }}(types.{{ camel_case_app_name }}OutputMutation, Mutation):
    class Arguments:
        where = types.{{ camel_case_app_name }}WhereUniqueInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ camel_case_app_name }}, _info: ResolveInfo, where: types.{{ camel_case_app_name }}WhereUniqueInput,
    ) -> models.{{ camel_case_app_name }}:
        return data.delete_{{ app_name }}(where)


class Query(ObjectType):
    {{ app_name }} = Field(types.Starship, where=types.{{ camel_case_app_name }}WhereUniqueInput(required=True))
    {{ app_name }}s = Field(List(NonNull(types.{{ camel_case_app_name }})), where=types.{{ camel_case_app_name }}WhereInput())

    def resolve_starships(
        _root: models.{{ camel_case_app_name }}, _info: ResolveInfo, where: types.{{ camel_case_app_name }}WhereInput = None,
    ) -> list[models.{{ camel_case_app_name }}]:
        return filters.{{ camel_case_app_name }}Filter(data=where).queryset

    def resolve_starship(
        _root: models.{{ camel_case_app_name }}, _info: ResolveInfo, where: types.{{ camel_case_app_name }}WhereUniqueInput,
    ) -> models.{{ camel_case_app_name }}:
        return data.get_{{ app_name }}(where)


class Mutation(ObjectType):
    create_{{ app_name }} = Create{{ camel_case_app_name }}.Field(required=True)
    update_{{ app_name }} = Update{{ camel_case_app_name }}.Field()
    delete_{{ app_name }} = Delete{{ camel_case_app_name }}.Field()
