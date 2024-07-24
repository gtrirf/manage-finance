from django import forms
from .models import TypeIcons, CreateType, Valyuta, Balance, Income, Outcome


class TypeIconsForm(forms.ModelForm):
    class Meta:
        model = TypeIcons
        fields = ['type_icon', 'name_icon']


class CreateTypeForm(forms.ModelForm):
    class Meta:
        model = CreateType
        fields = ['type_name', 'type_choice', 'type_icon']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_choice'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_icon'].widget.attrs.update({'class': 'form-control'})


class ValyutaForm(forms.ModelForm):
    class Meta:
        model = Valyuta
        fields = ['name_valyuta', 'code', 'symbol', 'rate_to_usd']


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['name', 'value', 'currency', 'comment', 'types']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['value'].widget.attrs.update({'class': 'form-control'})
        self.fields['currency'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})
        self.fields['types'].widget.attrs.update({'class': 'form-control'})


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['balance', 'amount', 'currency', 'comment', 'types']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['currency'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})
        self.fields['types'].widget.attrs.update({'class': 'form-control'})


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['balance', 'amount', 'currency', 'comment', 'types']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['currency'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})
        self.fields['types'].widget.attrs.update({'class': 'form-control'})