from django.urls import path
from .views import CountryListView, CountryDetailView, CountryCreateView, CountryUpdateView, CountryDeleteView

urlpatterns = [
    path('', CountryListView.as_view(), name='list_view'),
    path('<int:pk>', CountryDetailView.as_view(), name='detail_view'),
    path('create', CountryCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', CountryUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>', CountryDeleteView.as_view(), name='delete_view'),
    ]
