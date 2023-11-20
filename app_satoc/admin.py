from django.contrib import admin
from app_satoc.models import DomainFormat, DomainEPSG, DomainType
from app_satoc.models import OriginalFolderSource, OriginalFileName, FinalDatabase, FinalFileName

# Domain models
admin.site.register(DomainFormat)
admin.site.register(DomainEPSG)
admin.site.register(DomainType)


# Metadata models
class OriginalFileNameAdmin(admin.ModelAdmin):
    list_display = ('ofn_featureclass', 'ofn_featuredataset', 'ofn_ofs')
    ordering = ['ofn_ofs', 'ofn_featuredataset', 'ofn_featureclass']

class FinalFileNameAdmin(admin.ModelAdmin):
    list_display = ('ffn_featureclass', 'ffn_ofs', 'ffn_ofn', 'ffn_fdb')
    search_fields = ['ffn_ofn']  # Add search field if needed
    # Other configurations for PersonAdmin...

class FinalDatabaseAdmin(admin.ModelAdmin):
    list_display = ('fdb_database_name', 'fdb_database_active', 'fdb_webportal_active', 'fdb_moved')
    # Other configurations for PersonAdmin...

admin.site.register(OriginalFolderSource)
admin.site.register(OriginalFileName, OriginalFileNameAdmin)
admin.site.register(FinalFileName, FinalFileNameAdmin)
admin.site.register(FinalDatabase, FinalDatabaseAdmin)

# Users models