from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    photo = forms.ImageField()
    