from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as gl
import requests
from accounts.models import CustomUser as User


class TypeIcons(models.Model):
    type_icon = models.ImageField(upload_to='typeicons/')
    name_icon = models.CharField(max_length=100)

    class Meta:
        db_table = 'icons'

    def __str__(self):
        return self.name_icon


class CreateType(models.Model):
    INCOME = 'in'
    OUTCOME = 'out'
    FORBALANCE = 'blc'
    UNIVERSAL = 'uni'

    CHOICE = [
        (INCOME, 'income'),
        (OUTCOME, 'outcome'),
        (FORBALANCE, 'forbalance'),
        (UNIVERSAL, 'universal')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='choice')
    type_name = models.CharField(max_length=100)
    type_choice = models.CharField(max_length=3, choices=CHOICE, default=UNIVERSAL)
    type_icon = models.ForeignKey(TypeIcons, on_delete=models.CASCADE)

    class Meta:
        db_table = 'createdtypes'

    def __str__(self):
        return f'{self.type_choice} - {self.type_name} - {self.user}'


class Valyuta(models.Model):
    name_valyuta = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=10)
    rate_to_usd = models.DecimalField(max_digits=20, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = gl('Currency')
        verbose_name_plural = gl('Currencies')

    def __str__(self):
        return f'{self.name_valyuta} ({self.symbol})'

    @classmethod
    def update_exchange_rates(cls):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        for code, rate in data['rates'].items():
            valyuta, created = cls.objects.get_or_create(code=code, defaults={'rate_to_usd': rate, 'name_valyuta': code})
            if not created:
                valyuta.rate_to_usd = rate
            valyuta.save()


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balances')
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.ForeignKey(Valyuta, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, null=True)
    types = models.ForeignKey(CreateType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = gl('Balance')
        verbose_name_plural = gl('Balances')

    def __str__(self):
        return f'{self.name} - {self.value} {self.currency.symbol}'

    def convert_to_usd(self):
        return self.value / self.currency.rate_to_usd


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.ForeignKey(Valyuta, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
    types = models.ForeignKey(CreateType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = gl('Income')
        verbose_name_plural = gl('Incomes')

    def __str__(self):
        return f'{self.amount} {self.currency.symbol} - {self.types}'

    def save(self, *args, **kwargs):
        self.balance.value += self.amount / self.currency.rate_to_usd * self.balance.currency.rate_to_usd
        self.balance.save()
        super().save(*args, **kwargs)


class Outcome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outcomes')
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE, related_name='outcomes')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.ForeignKey(Valyuta, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
    types = models.ForeignKey(CreateType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = gl('Outcome')
        verbose_name_plural = gl('Outcomes')

    def __str__(self):
        return f'{self.amount} {self.currency.symbol} - {self.types}'

    def save(self, *args, **kwargs):
        self.balance.value -= self.amount / self.currency.rate_to_usd * self.balance.currency.rate_to_usd
        self.balance.save()
        super().save(*args, **kwargs)

