# Built-in packages

# Third-party packages
from django_filters import FilterSet

# Local packages
from . import models


class {{ camel_case_app_name }}Filter(FilterSet):
    class Meta:
        model = models.{{ camel_case_app_name }}
        fields = []