from django.db import models

# Create your models here.

class UploadFile(models.Model):
   name= models.CharField(max_length=200)
   file_up= models.FileField(upload_to= 'media/')

   def delete(self, using= None, keep_parents= False):  
      self.file_up.storage.delete(self.file_up.name)
      super().delete()
