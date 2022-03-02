import django_filters 

from .models import Table


class TableFilter(django_filters.FilterSet):
    class Meta:
        model = Table
        fields = '__all__'
    
    @property
    def qs(self):
        qs = super().qs
        data = {k: v for k, v in self.data.items() if k.startswith(tuple(self.get_fields().keys()))}
        return qs.filter(**data)