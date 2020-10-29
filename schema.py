# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from . import models, types, filters, crud


class Create{{ camel_case_app_name }}(types.{{ camel_case_app_name }}OutputMutation, gql.Mutation):
    class Arguments:
        data = types.DroidCreateInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ camel_case_app_name }}, _info: gql.ResolveInfo, data: types.DroidCreateInput,
    ) -> models.{{ camel_case_app_name }}:
        return crud.create_{{ app_name }}(data)


class Update{{ camel_case_app_name }}(types.{{ camel_case_app_name }}OutputMutation, gql.Mutation):
    class Arguments:
        where = types.{{ camel_case_app_name }}WhereUniqueInput(required=True)
        data = types.DroidUpdateInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ camel_case_app_name }}, _info: gql.ResolveInfo, where: types.{{ camel_case_app_name }}WhereUniqueInput, data: types.DroidUpdateInput,
    ) -> models.{{ camel_case_app_name }}:
        return crud.update_{{ app_name }}(where, data)


class Delete{{ camel_case_app_name }}(types.{{ camel_case_app_name }}OutputMutation, gql.Mutation):
    class Arguments:
        where = types.{{ camel_case_app_name }}WhereUniqueInput(required=True)

    @atomic
    def mutate(
        _root: models.{{ camel_case_app_name }}, _info: gql.ResolveInfo, where: types.{{ camel_case_app_name }}WhereUniqueInput,
    ) -> models.{{ camel_case_app_name }}:
        return crud.delete_{{ app_name }}(where)


class Query(gql.ObjectType):
    {{ app_name }} = gql.Field(types.{{ camel_case_app_name }}, where=types.{{ camel_case_app_name }}WhereUniqueInput(required=True))
    {{ app_name }}s = gql.Field(gql.List(gql.NonNull(types.{{ camel_case_app_name }})), where=types.{{ camel_case_app_name }}WhereInput())

    def resolve_{{ app_name }}(
        _root: models.{{ camel_case_app_name }}, _info: gql.ResolveInfo, where: types.{{ camel_case_app_name }}WhereUniqueInput,
    ) -> models.{{ camel_case_app_name }}:
        return crud.get_{{ app_name }}(where)

    def resolve_{{ app_name }}s(
        _root: models.{{ camel_case_app_name }}, _info: gql.ResolveInfo, where: types.{{ camel_case_app_name }}WhereInput = None,
    ) -> list[models.{{ camel_case_app_name }}]:
        return filters.{{ camel_case_app_name }}Filter(data=where).queryset


class Mutation(gql.ObjectType):
    create_{{ app_name }} = Create{{ camel_case_app_name }}.Field(required=True)
    update_{{ app_name }} = Update{{ camel_case_app_name }}.Field()
    delete_{{ app_name }} = Delete{{ camel_case_app_name }}.Field()
