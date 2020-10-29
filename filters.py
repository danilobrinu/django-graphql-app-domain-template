# Built-in packages

# Third-party packages
from django_filters import FilterSet

# Local packages
from .models import {{ camel_case_app_name }}


class {{ camel_case_app_name }}Filter(FilterSet):
    class Meta:
        model = {{ camel_case_app_name }}
        fields = []