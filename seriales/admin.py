from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Computador



# Register your models here.
class ComputadorResource(resources.ModelResource):
  class Meta:
    model = Computador
    fields = ('id','serial') 

class ComputadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = ComputadorResource

admin.site.register(Computador, ComputadorAdmin)