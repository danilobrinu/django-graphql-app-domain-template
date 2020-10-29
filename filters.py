# Built-in packages

# Third-party packages
from django_filters import FilterSet

# Local packages
from .models import {{ app_name }}


class {{ app_name }}Filter(FilterSet):
    class Meta:
        model = {{ app_name }}
        fields = []