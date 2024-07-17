"""
Содержит кастомные фильтры:

- Фильтр по виду питомца;
- ...
"""
import django_filters
from pet.models import Pet


class PetFilter(django_filters.FilterSet):
    """Кастомный фильтр по виду питомца"""
    type = django_filters.CharFilter(field_name='type__slug',
                                     lookup_expr='exact')

    class Meta:
        model = Pet
        fields = ['type']
