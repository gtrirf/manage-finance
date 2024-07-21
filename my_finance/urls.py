from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('incomes/', views.IncomeListView.as_view(), name='income_list'),
    path('incomes/new/', views.IncomeCreateView.as_view(), name='income_create'),
    path('outcomes/', views.OutcomeListView.as_view(), name='outcome_list'),
    path('outcomes/new/', views.OutcomeCreateView.as_view(), name='outcome_create'),
    path('balances/', views.BalanceListView.as_view(), name='balance_list'),
    path('balance/new/', views.BalanceCreateView.as_view(), name='balance_create'),
]
