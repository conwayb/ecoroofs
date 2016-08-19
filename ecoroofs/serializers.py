from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_field_names(self, *args, **kwargs):
        names = super().get_field_names(*args, **kwargs)
        if 'url' not in names:
            names.append('url')
        return names

    def get_extra_kwargs(self, *args, **kwargs):
        extra_kwargs = super().get_extra_kwargs(*args, **kwargs)
        if 'url' not in extra_kwargs:
            view = self.context['view']
            lookup_field = view.lookup_field
            extra_kwargs['url'] = {'lookup_field': lookup_field}
        return extra_kwargs

    @classmethod
    def from_model(cls, model, meta_attrs=None, **cls_attrs):
        # Returns a subclass configured with the specified model.
        meta_attrs = meta_attrs if meta_attrs is not None else {}
        meta_attrs['model'] = model
        cls_attrs['Meta'] = type('_Meta', (), meta_attrs)
        return type(cls.__name__, (cls,), cls_attrs)
