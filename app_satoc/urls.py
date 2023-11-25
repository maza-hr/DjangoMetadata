from django.urls import path
from app_satoc import views
from app_satoc.views import metadata_home, metadata_about, Detail_OFS, Detail_OFN, Detail_FFN, Detail_FDB

from app_satoc.views import feedback_view

app_name = 'metadata'

urlpatterns=[
    ## METADATA HOME PAGE
    path('', metadata_home, name='metadata_home'),
    path('about/', metadata_about, name='metadata_about'),
    
    path('ofs-list/', views.List_OriginalFolderSource.as_view(), name='ofs-list'),
    path('ofs-detail/<int:pk>/', Detail_OFS, name='ofs-detail'),
    
    path('ofn-list/', views.List_OriginalFileName.as_view(), name='ofn-list'),
    path('ofn-detail/<int:pk>/', Detail_OFN, name='ofn-detail'),
    
    path('ffn-list/', views.List_FinalFileName.as_view(), name='ffn-list'),
    path('ffn-detail/<int:pk>/', Detail_FFN, name='ffn-detail'),

    path('fdb-list/', views.List_FinalDatabase.as_view(), name='fdb-list'),
    path('fdb-detail/<int:pk>/', Detail_FDB, name='fdb-detail'),

    path('form/', feedback_view, name='form'),
]