from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin): #Con esta clase estamos agregando al paneel de addministrados la fecha de creacion y edicion
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
