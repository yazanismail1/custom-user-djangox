from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Country


class CountryTemplateView(TemplateView):
    template_name = 'countries/country_template_view.html'

class CountryListView(ListView):
    template_name = 'countries/country_list_view.html'
    model = Country
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    template_name = 'countries/country_detail_view.html'
    model = Country

class CountryCreateView(CreateView):
    template_name = 'countries/country_create_view.html'
    model = Country
    context_object_name = 'countries'
    fields = ["country_name", "continent", "capital_city", "flag_img", "time_zone", "national_dish", "author"]

class CountryUpdateView(UpdateView):
    template_name = 'countries/country_update_view.html'
    model = Country
    fields = ["country_name", "continent", "capital_city", "flag_img", "time_zone", "national_dish", "author"]
    success_url = reverse_lazy('list_view')

class CountryDeleteView(DeleteView):
    template_name = 'countries/country_delete_view.html'
    model = Country
    success_url = reverse_lazy('list_view')