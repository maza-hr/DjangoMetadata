from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.http.response import JsonResponse
from app_satoc.models import OriginalFolderSource, OriginalFileName, FinalFileName, FinalDatabase



def index(request):
    return render(request, 'shared/index.html')

def metadata_home(request):
    return render(request, 'app_satoc/metadata_home.html')

def metadata_about(request):
    return render(request, 'app_satoc/metadata_about.html')


### VIEWS FOR ORIGINAL FOLDER SOURCE
class List_OriginalFolderSource(ListView):
    model = OriginalFolderSource
    queryset = OriginalFolderSource.objects.all()

def Detail_OFS(request, pk):
    originalfoldersource = get_object_or_404(OriginalFolderSource, ofs_id=pk)
    finalfilename = FinalFileName.objects.filter(ffn_ofs=pk).select_related('ffn_ofn','ffn_fdb')
    
    context = {
        'originalfoldersource': originalfoldersource,
        'finalfilename': finalfilename
        }

    return render(request, 'app_satoc/originalfoldersource_detail.html', context)


### VIEWS FOR ORIGINAL FILE NAME
class List_OriginalFileName(ListView):
    model = OriginalFileName
    queryset = OriginalFileName.objects.all()

def Detail_OFN(request, pk):
    originalfilename = get_object_or_404(OriginalFileName, ofn_id=pk)
    finalfilename = FinalFileName.objects.filter(ffn_ofn=pk).select_related('ffn_ofs','ffn_fdb')
    
    context = {
        'originalfilename': originalfilename,
        'finalfilename': finalfilename
        }

    return render(request, 'app_satoc/originalfilename_detail.html', context)

### VIEWS FOR FINAL FEATURE NAME
class List_FinalFileName(ListView):
    model = FinalFileName
    queryset = FinalFileName.objects.all()

def Detail_FFN(request, pk):
    finalfilename = get_object_or_404(FinalFileName, ffn_id=pk)
    
    context = {
        'finalfilename': finalfilename
        }

    return render(request, 'app_satoc/finalfilename_detail.html', context)

### VIEWS FOR FINAL FEATURE DATASET
class List_FinalDatabase(ListView):
    model = FinalDatabase
    queryset = FinalDatabase.objects.all()

def Detail_FDB(request, pk):
    finaldatabase = get_object_or_404(FinalDatabase, fdb_id=pk)
    finalfilename = FinalFileName.objects.filter(ffn_fdb=pk).select_related('ffn_ofs','ffn_ofn')
    
    context = {
        'finaldatabase': finaldatabase,
        'finalfilename': finalfilename
        }

    return render(request, 'app_satoc/finaldatabase_detail.html', context)





### VIEWS FOR ARCGIS USERS AND FORM
# views.py

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from app_satoc.forms import FeedbackForm
#from prj_typsa_aztec.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD 
from django.conf import settings 

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Salvar os dados do formulário no banco de dados
            feedback = form.save()

            # Coletar os dados do formulario
            first_name = feedback.first_name
            last_name = feedback.last_name
            email = feedback.email
            company = feedback.company
            role_job_title = feedback.role_job_title

            # Criar a mensagem do e-mail e configurar quem envia e quem recebe
            subject = 'New User Request'
            message = f'A new request has send by an user.\n\nFirst Name: {first_name} \nLast Name:{last_name}\nRole or Job: {role_job_title}\nCompany: {company}\nEmail: {email}\nComentário: {role_job_title}'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['henrique.maza.ramos@gmail.com']

            print("Marcador")

            print(message)

            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, to_email)
                except BadHeaderError:
                    return HttpResponse("Invalid header found.")
                return render(request, 'app_form/form_success.html')

            else:
                return HttpResponse("Make sure all fields are entered and valid.")
    else:
        form = FeedbackForm()

    return render(request, 'app_form/form_send.html', {'form': form})  # Renderiza o formulário HTML
