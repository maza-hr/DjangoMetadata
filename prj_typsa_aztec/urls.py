from django.contrib import admin
from django.urls import path, include, re_path
from app_satoc.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('metadata/', include('app_satoc.urls')),
    path('', index, name='index'),
    re_path(r'^chaining/', include('smart_selects.urls')),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)