from django import forms
from .models import Income, Outcome, Balance


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value', 'type', 'date', 'comment', 'valyuta']


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['value', 'type', 'date', 'comment', 'valyuta']


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'type', 'date', 'comment', 'valyuta']
