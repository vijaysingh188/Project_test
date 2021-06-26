from django.contrib import admin
from .models import ToDo,UploadDocuments
admin.site.register(UploadDocuments)

# Register your models here.
admin.site.register(ToDo)