from django.db import models
from accounts.models import User


class Type(models.Model):
    type_name = models.CharField(max_length=100)
    type_icon = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.type_name


class Valyuta(models.Model):
    name_valyuta = models.CharField(max_length=200)
    price_per_dollar = models.DecimalField(max_digits=20, decimal_places=2)
    icon = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = 'valyuta'

    def __str__(self):
        return f'{self.name_valyuta} - {self.price_per_dollar}'


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_balances')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valyuta = models.ForeignKey(Valyuta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'balance'

    def __str__(self):
        return f'{self.user} - {self.value}'

    def convert_to_dollars(self, value, valyuta):
        if valyuta == self.valyuta:
            return value
        return value / valyuta.price_per_dollar

    def add_income(self, income):
        income_value_in_dollars = self.convert_to_dollars(income.value, income.valyuta)
        if income.user == self.user:
            self.value += income_value_in_dollars
            self.save()

    def subtract_outcome(self, outcome):
        outcome_value_in_dollars = self.convert_to_dollars(outcome.value, outcome.valyuta)
        if outcome.user == self.user:
            self.value -= outcome_value_in_dollars
            self.save()


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='income_balance')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valyuta = models.ForeignKey(Valyuta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'income'

    def __str__(self):
        return f'{self.user} - {self.value}'


class Outcome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outcome')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valyuta = models.ForeignKey(Valyuta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'outcome'

    def __str__(self):
        return f'{self.user} - {self.value}'
