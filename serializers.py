# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from .models import {{ camel_case_app_name }}


class {{ camel_case_app_name }}Serializer(ModelSerializer):
    class Meta:
        model = {{ camel_case_app_name }}
        fields = "__all__"
