# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from . import models


class {{ camel_case_app_name }}Serializer(ModelSerializer):
    class Meta:
        model = models.{{ camel_case_app_name }}
        fields = "__all__"
