from django.utils.timezone import now
from django.db.models import Sum
from datetime import timedelta
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TypeIcons, CreateType, Valyuta, Balance, Income, Outcome
from .forms import TypeIconsForm, CreateTypeForm, ValyutaForm, BalanceForm, IncomeForm, OutcomeForm
from .models import Valyuta


# def home(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#
#     return render(request, 'home.html')


def update_exchange_rates(request):
    Valyuta.update_exchange_rates()
    return JsonResponse({'status': 'Exchange rates updated'})


class TypeIconsListView(View):
    def get(self, request):
        typeicons = TypeIcons.objects.all()
        return render(request, 'typeicons_list.html', {'typeicons': typeicons})


# class TypeIconsCreateView(View):
#     def get(self, request):
#         form = TypeIconsForm()
#         return render(request, 'typeicons_form.html', {'form': form})
#
#     def post(self, request):
#         form = TypeIconsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('typeicons_list')
#         return render(request, 'typeicons_form.html', {'form': form})


# class TypeIconsUpdateView(View):
#     def get(self, request, pk):
#         typeicon = get_object_or_404(TypeIcons, pk=pk)
#         form = TypeIconsForm(instance=typeicon)
#         return render(request, 'typeicons_form.html', {'form': form})
#
#     def post(self, request, pk):
#         typeicon = get_object_or_404(TypeIcons, pk=pk)
#         form = TypeIconsForm(request.POST, request.FILES, instance=typeicon)
#         if form.is_valid():
#             form.save()
#             return redirect('typeicons_list')
#         return render(request, 'typeicons_form.html', {'form': form})


# class TypeIconsDeleteView(View):
#     def get(self, request, pk):
#         typeicon = get_object_or_404(TypeIcons, pk=pk)
#         return render(request, 'typeicons_confirm_delete.html', {'typeicon': typeicon})
#
#     def post(self, request, pk):
#         typeicon = get_object_or_404(TypeIcons, pk=pk)
#         typeicon.delete()
#         return redirect('typeicons_list')

# CreateType Views
class CreateTypeListView(View):
    def get(self, request):
        createtypes = CreateType.objects.all()
        return render(request, 'createtype_list.html', {'createtypes': createtypes})


class CreateTypeCreateView(View):
    def get(self, request):
        form = CreateTypeForm()
        return render(request, 'createtype_form.html', {'form': form})

    def post(self, request):
        form = CreateTypeForm(request.POST, request.FILES)
        if form.is_valid():
            createtype = form.save(commit=False)
            createtype.user = request.user
            createtype.save()
            return redirect('createtype_list')
        return render(request, 'createtype_form.html', {'form': form})


class CreateTypeUpdateView(View):
    def get(self, request, pk):
        createtype = get_object_or_404(CreateType, pk=pk, user=request.user)
        form = CreateTypeForm(instance=createtype)
        return render(request, 'createtype_form.html', {'form': form})

    def post(self, request, pk):
        createtype = get_object_or_404(CreateType, pk=pk, user=request.user)
        form = CreateTypeForm(request.POST, request.FILES, instance=createtype)
        if form.is_valid():
            form.save()
            return redirect('createtype_list')
        return render(request, 'createtype_form.html', {'form': form})


class CreateTypeDeleteView(View):
    def get(self, request, pk):
        createtype = get_object_or_404(CreateType, pk=pk, user=request.user)
        return render(request, 'createtype_confirm_delete.html', {'createtype': createtype})

    def post(self, request, pk):
        createtype = get_object_or_404(CreateType, pk=pk, user=request.user)
        createtype.delete()
        return redirect('createtype_list')

class ValyutaListView(View):
    def get(self, request):
        valyutas = Valyuta.objects.all()
        return render(request, 'valyuta_list.html', {'valyutas': valyutas})


# class ValyutaCreateView(View):
#     def get(self, request):
#         form = ValyutaForm()
#         return render(request, 'valyuta_form.html', {'form': form})
#
#     def post(self, request):
#         form = ValyutaForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('valyuta_list')
#         return render(request, 'valyuta_form.html', {'form': form})


# class ValyutaUpdateView(View):
#     def get(self, request, pk):
#         valyuta = get_object_or_404(Valyuta, pk=pk)
#         form = ValyutaForm(instance=valyuta)
#         return render(request, 'valyuta_form.html', {'form': form})
#
#     def post(self, request, pk):
#         valyuta = get_object_or_404(Valyuta, pk=pk)
#         form = ValyutaForm(request.POST, request.FILES, instance=valyuta)
#         if form.is_valid():
#             form.save()
#             return redirect('valyuta_list')
#         return render(request, 'valyuta_form.html', {'form': form})


# class ValyutaDeleteView(View):
#     def get(self, request, pk):
#         valyuta = get_object_or_404(Valyuta, pk=pk)
#         return render(request, 'valyuta_confirm_delete.html', {'valyuta': valyuta})
#
#     def post(self, request, pk):
#         valyuta = get_object_or_404(Valyuta, pk=pk)
#         valyuta.delete()
#         return redirect('valyuta_list')


class BalanceListView(View):
    def get(self, request):
        balances = Balance.objects.filter(user=request.user)
        return render(request, 'balance_list.html', {'balances': balances})


class BalanceCreateView(View):
    def get(self, request):
        form = BalanceForm()
        return render(request, 'balance_form.html', {'form': form})

    def post(self, request):
        form = BalanceForm(request.POST, request.FILES)
        if form.is_valid():
            balance = form.save(commit=False)
            balance.user = request.user
            balance.save()
            return redirect('balance_list')
        return render(request, 'balance_form.html', {'form': form})


class BalanceUpdateView(View):
    def get(self, request, pk):
        balance = get_object_or_404(Balance, pk=pk, user=request.user)
        form = BalanceForm(instance=balance)
        return render(request, 'balance_form.html', {'form': form})

    def post(self, request, pk):
        balance = get_object_or_404(Balance, pk=pk, user=request.user)
        form = BalanceForm(request.POST, request.FILES, instance=balance)
        if form.is_valid():
            form.save()
            return redirect('balance_list')
        return render(request, 'balance_form.html', {'form': form})


class BalanceDeleteView(View):
    def get(self, request, pk):
        balance = get_object_or_404(Balance, pk=pk, user=request.user)
        return render(request, 'balance_confirm_delete.html', {'balance': balance})

    def post(self, request, pk):
        balance = get_object_or_404(Balance, pk=pk, user=request.user)
        balance.delete()
        return redirect('balance_list')


class IncomeListView(View):
    def get(self, request):
        incomes = Income.objects.filter(user=request.user)
        return render(request, 'income_list.html', {'incomes': incomes})


class IncomeCreateView(View):
    def get(self, request):
        form = IncomeForm()
        return render(request, 'income_form.html', {'form': form})

    def post(self, request):
        form = IncomeForm(request.POST, request.FILES)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
        return render(request, 'income_form.html', {'form': form})


class IncomeUpdateView(View):
    def get(self, request, pk):
        income = get_object_or_404(Income, pk=pk, user=request.user)
        form = IncomeForm(instance=income)
        return render(request, 'income_form.html', {'form': form})

    def post(self, request, pk):
        income = get_object_or_404(Income, pk=pk, user=request.user)
        form = IncomeForm(request.POST, request.FILES, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
        return render(request, 'income_form.html', {'form': form})


class IncomeDeleteView(View):
    def get(self, request, pk):
        income = get_object_or_404(Income, pk=pk, user=request.user)
        return render(request, 'income_confirm_delete.html', {'income': income})

    def post(self, request, pk):
        income = get_object_or_404(Income, pk=pk, user=request.user)
        income.delete()
        return redirect('income_list')


class OutcomeListView(View):
    def get(self, request):
        outcomes = Outcome.objects.filter(user=request.user)
        return render(request, 'outcome_list.html', {'outcomes': outcomes})


class OutcomeCreateView(View):
    def get(self, request):
        form = OutcomeForm()
        return render(request, 'outcome_form.html', {'form': form})

    def post(self, request):
        form = OutcomeForm(request.POST, request.FILES)
        if form.is_valid():
            outcome = form.save(commit=False)
            outcome.user = request.user
            outcome.save()
            return redirect('outcome_list')
        return render(request, 'outcome_form.html', {'form': form})


class OutcomeUpdateView(View):
    def get(self, request, pk):
        outcome = get_object_or_404(Outcome, pk=pk, user=request.user)
        form = OutcomeForm(instance=outcome)
        return render(request, 'outcome_form.html', {'form': form})

    def post(self, request, pk):
        outcome = get_object_or_404(Outcome, pk=pk, user=request.user)
        form = OutcomeForm(request.POST, request.FILES, instance=outcome)
        if form.is_valid():
            form.save()
            return redirect('outcome_list')
        return render(request, 'outcome_form.html', {'form': form})

class OutcomeDeleteView(View):
    def get(self, request, pk):
        outcome = get_object_or_404(Outcome, pk=pk, user=request.user)
        return render(request, 'outcome_confirm_delete.html', {'outcome': outcome})

    def post(self, request, pk):
        outcome = get_object_or_404(Outcome, pk=pk, user=request.user)
        outcome.delete()
        return redirect('outcome_list')


class ChartView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'charts.html')


class IncomeOutcomeData(View):
    def get(self, request, period):
        today = now().date()
        data = {
            'labels': [],
            'incomes': [],
            'outcomes': [],
        }

        if period == 'daily':
            for i in range(0, 7):
                day = today - timedelta(days=i)
                data['labels'].insert(0, day.strftime('%Y-%m-%d'))
                income_sum = Income.objects.filter(user=request.user, date__date=day).aggregate(Sum('amount'))['amount__sum'] or 0
                outcome_sum = Outcome.objects.filter(user=request.user, date__date=day).aggregate(Sum('amount'))['amount__sum'] or 0
                data['incomes'].insert(0, income_sum)
                data['outcomes'].insert(0, outcome_sum)

        elif period == 'weekly':
            for i in range(0, 4):
                start_week = today - timedelta(weeks=i)
                end_week = start_week + timedelta(days=6)
                data['labels'].insert(0, f'{start_week.strftime("%Y-%m-%d")} - {end_week.strftime("%Y-%m-%d")}')
                income_sum = Income.objects.filter(user=request.user, date__date__range=[start_week, end_week]).aggregate(Sum('amount'))['amount__sum'] or 0
                outcome_sum = Outcome.objects.filter(user=request.user, date__date__range=[start_week, end_week]).aggregate(Sum('amount'))['amount__sum'] or 0
                data['incomes'].insert(0, income_sum)
                data['outcomes'].insert(0, outcome_sum)

        elif period == 'monthly':
            for i in range(0, 12):
                month = today - timedelta(days=i*30)
                month_start = month.replace(day=1)
                next_month_start = (month_start + timedelta(days=32)).replace(day=1)
                data['labels'].insert(0, month.strftime('%Y-%m'))
                income_sum = Income.objects.filter(user=request.user, date__date__range=[month_start, next_month_start]).aggregate(Sum('amount'))['amount__sum'] or 0
                outcome_sum = Outcome.objects.filter(user=request.user, date__date__range=[month_start, next_month_start]).aggregate(Sum('amount'))['amount__sum'] or 0
                data['incomes'].insert(0, income_sum)
                data['outcomes'].insert(0, outcome_sum)

        elif period == 'yearly':
            for i in range(0, 5):
                year = today.year - i
                data['labels'].insert(0, str(year))
                income_sum = Income.objects.filter(user=request.user, date__year=year).aggregate(Sum('amount'))['amount__sum'] or 0
                outcome_sum = Outcome.objects.filter(user=request.user, date__year=year).aggregate(Sum('amount'))['amount__sum'] or 0
                data['incomes'].insert(0, income_sum)
                data['outcomes'].insert(0, outcome_sum)

        return JsonResponse(data)