from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin




class PredicionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('type_refuses', 'type_gpa', 'type_say', 'type_equioment', 'element', 'maybe_reasons', 'meropriation',)




# Register your models here.

admin.site.register(Predicions, PredicionsAdmin)


