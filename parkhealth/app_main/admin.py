from parkhealth.app_main.models import MedicalStaff, Degree, Specialty
from django.contrib import admin

class DegreeAdmin(admin.ModelAdmin):
    list_display = ['acronym', 'name']

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['name', 'handle']

class MedicalAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'name_last', 'name_first']
    ordering = ['name_last', 'name_first']

admin.site.register(MedicalStaff, MedicalAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Specialty, SpecialtyAdmin)

