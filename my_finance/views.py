from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Balance, Income, Outcome
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import BalanceForm, IncomeForm, OutcomeForm


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'home.html')


class IncomeListView(View):
    @method_decorator(login_required)
    def get(self, request):
        incomes = Income.objects.filter(user=request.user)
        return render(request, 'finance/income_list.html', {'incomes': incomes})


class IncomeCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = IncomeForm()
        return render(request, 'finance/income_create.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            balance = Balance.objects.filter(user=request.user, valyuta=income.valyuta).first()
            if balance:
                balance.add_income(income)
            return redirect('income_list')
        return render(request, 'finance/income_create.html', {'form': form})


class OutcomeListView(View):
    @method_decorator(login_required)
    def get(self, request):
        outcomes = Outcome.objects.filter(user=request.user)
        return render(request, 'finance/outcome_list.html', {'outcomes': outcomes})


class OutcomeCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = OutcomeForm()
        return render(request, 'finance/outcome_create.html', {'form': form})

    def post(self, request):
        form = OutcomeForm(request.POST)
        if form.is_valid():
            outcome = form.save(commit=False)
            outcome.user = request.user
            outcome.save()
            balance = Balance.objects.filter(user=request.user, valyuta=outcome.valyuta).first()
            if balance:
                balance.subtract_outcome(outcome)
            return redirect('outcome_list')
        return render(request, 'finance/outcome_create.html', {'form': form})


class BalanceListView(View):
    @method_decorator(login_required)
    def get(self, request):
        balances = Balance.objects.filter(user=request.user)
        return render(request, 'finance/balance_list.html', {'balances': balances})


class BalanceCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = BalanceForm()
        return render(request, 'finance/balance_create.html', {'form': form})

    def post(self, request):
        form = BalanceForm(request.user)
        if form.is_valid():
            balance = form.save(commit=False)
            balance.user = request.user
            balance.save()
            return redirect('balance_list')
        return render(request, 'finance/balance_create.html', {'form': form})
