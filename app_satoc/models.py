from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# --------------- DOMAIN MODELS MODELS ---------------
# Format of files: "shp", "xls", "csv", etc.
class DomainFormat(models.Model):
    dom_sg_format = models.CharField(primary_key=True, max_length=4, verbose_name="Format Acronym")
    dom_nm_format = models.CharField(max_length=30, unique=True, verbose_name="Format Name")
 
    def __str__(self):
        return '{0} ({1})'.format(self.dom_nm_format, self.dom_sg_format)

# Coordinate system code
class DomainEPSG(models.Model):
    dom_cd_epsg = models.BigIntegerField(primary_key=True, verbose_name="EPSG Code")
    dom_sg_epsg = models.CharField(max_length=20, verbose_name="EPSG Acronym")
    dom_nm_epsg = models.CharField(max_length=30, verbose_name="EPSG Name")

    def __str__(self):
        return '{0} ({1})'.format(self.dom_sg_epsg, self.dom_cd_epsg)

# Type of data: polygon, line, raster, etc.   
class DomainType(models.Model):
    dom_cd_type = models.BigAutoField(primary_key=True, verbose_name="Type code")
    dom_sg_type = models.CharField(max_length=10, unique=True, verbose_name="Type Acronym")
    dom_nm_type = models.CharField(max_length=30, unique=True, verbose_name="Type Name")

    def __str__(self):
        # Cria o formato dom_nm_type (dom_sg_type) para exibição
        return '{0} ({1})'.format(self.dom_nm_type, self.dom_sg_type)

# --------------- METADATA MODELS ---------------

class OriginalFolderSource(models.Model):
    ofs_id = models.BigAutoField(primary_key=True, verbose_name="Primary Key")
    ofs_name = models.CharField(max_length=80, unique=True, verbose_name="Name")
    ofs_receiptdate = models.DateField(blank=True, null=True, verbose_name="Receipt Date")
    ofs_meansofreceipt = models.CharField(max_length=20, blank=True, null=True, verbose_name="Means of Receipt")
    ofs_storageplace = models.CharField(max_length=150, blank=True, null=True, verbose_name="Storage Place")  ### Considering to use models.FilePathField
    ofs_size = models.IntegerField(blank=True, null=True, verbose_name="Size (MB)")
    ofs_featureclass = models.SmallIntegerField(blank=True, null=True, verbose_name="Number of feature classes")
    ofs_format = models.ForeignKey(DomainFormat, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Format")
    ofs_email = models.BooleanField(default=False, verbose_name="Email attached")
    ofs_description = models.TextField(null=True, blank=True, verbose_name="Description")
 
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.ofs_name

class OriginalFileName(models.Model):
    ofn_id = models.BigAutoField(primary_key=True, verbose_name="Primary Key")
    ofn_ofs = models.ForeignKey(OriginalFolderSource, on_delete=models.DO_NOTHING, verbose_name="Original Folder Name",)
    ofn_featureclass = models.CharField(max_length=80, unique=True, blank=True, null=True, verbose_name="Original Feature Class Name")
    ofn_featuredataset = models.CharField(max_length=80, verbose_name="Original Feature Dataset Name")
    ofn_attributes = models.SmallIntegerField(blank=True, null=True, verbose_name="Number of attributes")
    ofn_epsg = models.ForeignKey(DomainEPSG, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="EPSG")
    ofn_format = models.ForeignKey(DomainFormat, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Format")
    ofn_type = models.ForeignKey(DomainType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Type")
    ofn_attached_photos = models.BooleanField(default=False, verbose_name="Attached photos")
    ofn_description = models.TextField(null=True, blank=True, verbose_name="Description")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.ofn_featureclass

class FinalDatabase(models.Model):
    fdb_id = models.BigAutoField(primary_key=True, verbose_name="Primary Key")
    fdb_database_name = models.CharField(max_length=80, unique=True, verbose_name="Final Database Name")
    fdb_storageplace = models.CharField(max_length=150, blank=True, null=True, verbose_name="Storage Place")                    ### Considering to use models.FilePathField
    fdb_format = models.ForeignKey(DomainFormat, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Format")
    fdb_database_active = models.BooleanField(default=False, verbose_name="Database is Active")
    fdb_webportal_active = models.BooleanField(default=False, verbose_name="Webportal is Active")
    fdb_moved = models.BooleanField(default=False, verbose_name="Files were totally moved")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.fdb_database_name

class FinalFileName(models.Model):
    ffn_id = models.BigAutoField(primary_key=True, verbose_name="Primary Key")
    ffn_ofs = models.ForeignKey(OriginalFolderSource, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Original Folder Source")
    ffn_ofn = ChainedForeignKey(
                                OriginalFileName,
                                chained_field="ffn_ofs",
                                chained_model_field="ofn_ofs",
                                show_all=False,
                                auto_choose=True,
                                sort=True,
                                verbose_name="Original File Name")
    ffn_fdb = models.ForeignKey(FinalDatabase, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Final Database")
    ffn_featureclass = models.CharField(max_length=80, unique=True, verbose_name="Final Feature Class Name")
    ffn_featuredataset = models.CharField(max_length=80, verbose_name="Final Feature Dataset Name")
    ffn_standard_sdsfie = models.BooleanField(default=False, verbose_name="Adheres to the SDSFIE standard")
    ffn_type = models.ForeignKey(DomainType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Type")
    ffn_format = models.ForeignKey(DomainFormat, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Format")
    ffn_epsg = models.ForeignKey(DomainEPSG, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="EPSG")
    ffn_description = models.TextField(null=True, blank=True, verbose_name="Description")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.ffn_featureclass