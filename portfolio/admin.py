from django.contrib import admin
from .models import Project

# Register your models here.

#extender las funcionalidades del administrador
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Project,ProjectAdmin)