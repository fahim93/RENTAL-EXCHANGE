from django.forms import ModelForm, CheckboxSelectMultiple

from rental_exchange.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        widgets = {
            'features': CheckboxSelectMultiple(),
        }
        fields = '__all__'
