# Built-in packages

# Third-party packages
import django_filters as df

# Local packages
from . import models


class {{ camel_case_app_name }}Filter(df.FilterSet):
    class Meta:
        model = models.{{ camel_case_app_name }}
        fields = []