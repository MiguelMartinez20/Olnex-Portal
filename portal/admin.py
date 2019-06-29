from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee, Contrato

#admin.site.register(Employee)

admin.site.register(Contrato)

@admin.register(Employee)
class ViewAdmin(ImportExportModelAdmin):
    pass

