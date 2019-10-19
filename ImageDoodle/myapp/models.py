from django.db import models
from django.contrib import admin
from system.storage import ImageStorage
from django.template.loader import  render_to_string
# Create your models here.

class DoodleImage(models.Model):
        image = models.ImageField(upload_to='./static',storage=ImageStorage())
        name= models.CharField(max_length=30)
        style = models.CharField(max_length=30)
        def __unicode__(self):
            return self.name

class ImaginAdmin(admin.ModelAdmin):
    list_display=["__unicode__","name","image","style"]

    def save_model(self, request, obj, form, change):
        obj.user=request.user
        obj.save()

admin.site.register(DoodleImage,ImaginAdmin)
