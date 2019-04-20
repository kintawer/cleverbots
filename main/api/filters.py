import django_filters

from main.models import Image


class ImagesFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='create_date')
    size = django_filters.NumberFilter(method='filter_size')

    class Meta:
        model = Image
        fields = ['date', 'size']

    # Фильтор по размеру картинки, именно по занимаемому месту в байтах
    # берет картинки меньше или ровно указанного размера
    def filter_size(self, queryset, name, value):
        return queryset.filter(pk__in=[item.pk for item in queryset if item.content.size <= value])
