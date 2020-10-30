# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers

# Local packages
from . import models


class {{ camel_case_app_name }}Serializer(drf_serializers.ModelSerializer):
    class Meta:
        model = models.{{ camel_case_app_name }}
        fields = "__all__"
