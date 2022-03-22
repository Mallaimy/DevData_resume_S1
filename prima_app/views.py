from django.shortcuts import redirect, render
from django.template import context
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from prima_app.models import Client

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class RecepLoginView(LoginView):
    template_name = 'prima_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('clients')



# Here goes my code for the CRUD Operations

class ClientList(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['clients'] = context['clients'].filter(
                nom_prenom__startwith=search_input)
            context['search_input'] = search_input
        return context


class ClientDetail(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'



class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['nom_prenom','sexe','age','telephone','date','categorie_imagerie','prix','medecin','decription_res']
    success_url = reverse_lazy('clients')

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(ClientCreate, self).form_valid(form)



class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('clients')


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    context_object_name = 'client'
    success_url = reverse_lazy('clients')