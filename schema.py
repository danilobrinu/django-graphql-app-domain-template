# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import Field, List, NonNull, ObjectType, Mutation, ResolveInfo

# Local packages
from . import models, types, data


class Create{{ app_name }}(types.{{ app_name }}OutputMutation, Mutation):
    class Arguments:
        data = types.DroidCreateInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ app_name }}, _info: ResolveInfo, data: types.DroidCreateInput,
    ) -> models.{{ app_name }}:
        return data.create_{{ camel_case_app_name }}(data)


class Update{{ app_name }}(types.{{ app_name }}OutputMutation, Mutation):
    class Arguments:
        where = types.{{ app_name }}WhereUniqueInput(required=True)
        data = types.DroidUpdateInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ app_name }}, _info: ResolveInfo, where: types.{{ app_name }}WhereUniqueInput, data: types.DroidUpdateInput,
    ) -> models.{{ app_name }}:
        return data.update_{{ camel_case_app_name }}(where, data)


class Delete{{ app_name }}(types.{{ app_name }}OutputMutation, Mutation):
    class Arguments:
        where = types.{{ app_name }}WhereUniqueInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ app_name }}, _info: ResolveInfo, where: types.{{ app_name }}WhereUniqueInput,
    ) -> models.{{ app_name }}:
        return data.delete_{{ camel_case_app_name }}(where)


class Query(ObjectType):
    {{ camel_case_app_name }} = Field(types.Starship, where=types.{{ app_name }}WhereUniqueInput(required=True))
    {{ camel_case_app_name }}s = Field(List(NonNull(types.{{ app_name }})), where=types.{{ app_name }}WhereInput())

    def resolve_starships(
        _root: models.{{ app_name }}, _info: ResolveInfo, where: types.{{ app_name }}WhereInput = None,
    ) -> list[models.{{ app_name }}]:
        return filters.{{ app_name }}Filter(data=where).queryset

    def resolve_starship(
        _root: models.{{ app_name }}, _info: ResolveInfo, where: types.{{ app_name }}WhereUniqueInput,
    ) -> models.{{ app_name }}:
        return get_{{ camel_case_app_name }}(where)


class Mutation(ObjectType):
    create_{{ camel_case_app_name }} = Create{{ app_name }}.Field(required=True)
    update_{{ camel_case_app_name }} = Update{{ app_name }}.Field()
    delete_{{ camel_case_app_name }} = Delete{{ app_name }}.Field()
