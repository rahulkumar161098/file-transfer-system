from django.contrib import admin
from .models import UploadFile

# Register your models here.
class fileView(admin.ModelAdmin):
   list_display=('id','name','file_up', )
admin.site.register(UploadFile, fileView)
