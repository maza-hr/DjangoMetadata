from django.urls import path
from app_satoc import views
from app_satoc.views import metadata_home

app_name = 'metadata'

urlpatterns=[
    ## METADATA HOME PAGE
    path('', metadata_home, name='metadata_home'),
]