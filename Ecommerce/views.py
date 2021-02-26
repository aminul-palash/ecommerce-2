from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from book.models import Book
from django.views.generic.detail import DetailView 

# Create your views here.
class home(ListView):
  model=Book
  template_name = 'home/home.html'

class BookDetailView(DetailView):
  model = Book

