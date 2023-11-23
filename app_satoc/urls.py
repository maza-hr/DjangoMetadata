from django.urls import path
from app_satoc import views
from app_satoc.views import metadata_home, finalfeaturename, Detail_OFS

app_name = 'metadata'

urlpatterns=[
    ## METADATA HOME PAGE
    path('', metadata_home, name='metadata_home'),
    path('finalfeaturename', finalfeaturename, name='finalfeaturename'),
    path('ofs-list/', views.List_OriginalFolderSource.as_view(), name='ofs-list'),
    path('ofs-detail/<int:pk>/', Detail_OFS, name='ofs-detail'),
    path('teste/<int:pk>/', Detail_OFS, name='ofs-detail2'),
]