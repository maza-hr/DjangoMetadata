from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.http.response import JsonResponse


# from .forms import Form_FinalFileName
# from app_satoc.models import OriginalFolderSource, OriginalFileName, FinalFileName
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html')

def metadata_home(request):
    return render(request, 'app_satoc/metadata_home.html')