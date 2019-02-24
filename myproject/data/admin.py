from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AdultData

# @admin.register(AdultData)
# class AdultData(ImportExportModelAdmin):
#     pass


class Adultadmin(admin.ModelAdmin):
    list_display = ('age', 'workclass', 'fnl_wgt','education','education_num','maritalstatus','occupation','relationship','race','sex',
                    'capital_gain','capital_loss','hours_per_week','native_country')
    search_fields = ('sex', 'race', 'relationship')
    list_filter = ('sex', 'race', 'relationship')

admin.site.register(AdultData,Adultadmin)
