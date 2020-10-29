# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from .models import {{ app_name }}


class {{ app_name }}Serializer(ModelSerializer):
    class Meta:
        model = {{ app_name }}
        fields = "__all__"
