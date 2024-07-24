from django.contrib import admin
from .models import TypeIcons, CreateType, Balance, Income, Outcome, Valyuta

admin.site.register(TypeIcons)
admin.site.register(CreateType)
admin.site.register(Balance)
admin.site.register(Income)
admin.site.register(Outcome)
admin.site.register(Valyuta)
