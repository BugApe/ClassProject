from django.db import models
from django.contrib import admin
from django.template.loader import  render_to_string
# Create your models here.

class StyleImage(models.Model):
        image = models.ImageField(upload_to='images/')
        name= models.CharField(max_length=30)
        style = models.CharField(max_length=30)
        def __unicode__(self):
            return self.name

class ImaginAdmin(admin.ModelAdmin):
    list_display=["__unicode__","name","image","style"]

    def save_model(self, request, obj, form, change):
        obj.user=request.user
        obj.save()

admin.site.register(StyleImage,ImaginAdmin)
