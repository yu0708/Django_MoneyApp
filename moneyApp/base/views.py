from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import List

class ListList(ListView):
    model = List
    context_object_name = 'lists'

class ListDetail(DetailView):
    template_name = 'base/list_detail.html'
    context_object_name = 'list'
    model = List