from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    TypeIconsListView, CreateTypeListView, CreateTypeCreateView, CreateTypeUpdateView,
    CreateTypeDeleteView, ValyutaListView, BalanceListView, BalanceCreateView,
    BalanceUpdateView, BalanceDeleteView, IncomeListView, IncomeCreateView,
    IncomeUpdateView, IncomeDeleteView, OutcomeListView, OutcomeCreateView,
    OutcomeUpdateView, OutcomeDeleteView, ChartView, IncomeOutcomeData, update_exchange_rates
)

urlpatterns = [
    path('', views.ChartView.as_view(), name='charts-home'),
    path('income-outcome-data/<str:period>/', views.IncomeOutcomeData.as_view(), name='income_outcome_data'),
    path('update_exchange_rates/', update_exchange_rates, name='update_exchange_rates'), # valyuta kursini abnavit qilish uchun

    # TypeIcons URLs
    # path('typeicons/', TypeIconsListView.as_view(), name='typeicons_list'),
    # path('typeicons/create/', TypeIconsCreateView.as_view(), name='typeicons_create'),
    # path('typeicons/<int:pk>/update/', TypeIconsUpdateView.as_view(), name='typeicons_update'),
    # path('typeicons/<int:pk>/delete/', TypeIconsDeleteView.as_view(), name='typeicons_delete'),

    # CreateType URLs
    path('createtype/', CreateTypeListView.as_view(), name='createtype_list'),
    path('createtype/create/', CreateTypeCreateView.as_view(), name='createtype_create'),
    path('createtype/<int:pk>/update/', CreateTypeUpdateView.as_view(), name='createtype_update'),
    path('createtype/<int:pk>/delete/', CreateTypeDeleteView.as_view(), name='createtype_delete'),

    # Valyuta URLs
    path('valyuta/', ValyutaListView.as_view(), name='valyuta_list'),
    # path('valyuta/create/', ValyutaCreateView.as_view(), name='valyuta_create'),
    # path('valyuta/<int:pk>/update/', ValyutaUpdateView.as_view(), name='valyuta_update'),
    # path('valyuta/<int:pk>/delete/', ValyutaDeleteView.as_view(), name='valyuta_delete'),

    # Balance URLs
    path('balance/', BalanceListView.as_view(), name='balance_list'),
    path('balance/create/', BalanceCreateView.as_view(), name='balance_create'),
    path('balance/<int:pk>/update/', BalanceUpdateView.as_view(), name='balance_update'),
    path('balance/<int:pk>/delete/', BalanceDeleteView.as_view(), name='balance_delete'),

    # Income URLs
    path('income/', IncomeListView.as_view(), name='income_list'),
    path('income/create/', IncomeCreateView.as_view(), name='income_create'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name='income_update'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income_delete'),

    # Outcome URLs
    path('outcome/', OutcomeListView.as_view(), name='outcome_list'),
    path('outcome/create/', OutcomeCreateView.as_view(), name='outcome_create'),
    path('outcome/<int:pk>/update/', OutcomeUpdateView.as_view(), name='outcome_update'),
    path('outcome/<int:pk>/delete/', OutcomeDeleteView.as_view(), name='outcome_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)