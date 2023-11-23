from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.http.response import JsonResponse
from app_satoc.models import OriginalFolderSource, OriginalFileName, FinalFileName


# from .forms import Form_FinalFileName
# from app_satoc.models import OriginalFolderSource, OriginalFileName, FinalFileName
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'shared/index.html')

def metadata_home(request):
    return render(request, 'app_satoc/metadata_home.html')

### VIEWS FOR ORIGINAL FOLDER SOURCE

class List_OriginalFolderSource(ListView):
    model = OriginalFolderSource
    queryset = OriginalFolderSource.objects.all()

class Detail_OriginalFolderSource(DetailView):
    queryset = OriginalFolderSource.objects.all()
    fields = '__all__'
    success_url = reverse_lazy('metadata:detail')

def Detail_OFS(request, pk):
    originalfoldersource = get_object_or_404(OriginalFolderSource, ofs_id=pk)
    finalfilename = FinalFileName.objects.filter(ffn_ofs=pk).select_related('ffn_ofn','ffn_fdb')
    
    print(finalfilename[0].ffn_ofn)
    
    context = {
        'originalfoldersource': originalfoldersource,
        'finalfilename': finalfilename
        }

    return render(request, 'app_satoc/originalfoldersource_detail.html', context)

### VIEWS FOR ORIGINAL FILE NAME


### VIEWS FOR FINAL FEATURE NAME
def finalfeaturename(request):
    return render(request, 'app_satoc/finalfeaturename.html')

### VIEWS FOR FINAL FEATURE DATASET

### ABOUT