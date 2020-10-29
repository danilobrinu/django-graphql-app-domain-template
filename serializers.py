# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from . import models


class {{ camel_case_app_name }}Serializer(drf.serializers.ModelSerializer):
    class Meta:
        model = models.{{ camel_case_app_name }}
        fields = "__all__"
