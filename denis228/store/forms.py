from django import forms
from .models import Product, RepairService, City, RepairRequest
from django.utils.translation import gettext_lazy as _

class EstimateForm(forms.Form):
    device = forms.ModelChoiceField(queryset=Product.objects.filter(available=True), label="Название устройства")
    issue = forms.ModelChoiceField(queryset=RepairService.objects.all(), label="Что случилось с устройством")
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Город")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device'].queryset = Product.objects.filter(available=True)
        self.fields['issue'].queryset = RepairService.objects.all()
        self.fields['city'].queryset = City.objects.all()


class OrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Количество', initial=1)

class CreateRepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['contact_name', 'device_type', 'issue_description', 'contact_email', 'contact_phone']
        labels = {
            'contact_name': _('Имя клиента'),
            'device_type': _('Тип устройства'),
            'issue_description': _('Описание проблемы'),
            'contact_email': _('Контактный email'),
            'contact_phone': _('Контактный телефон'),
        }
        widgets = {
            'issue_description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class AdminResponseForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['response']
        labels = {
            'response': _('Ответ администратора'),
        }
        widgets = {
            'response': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
