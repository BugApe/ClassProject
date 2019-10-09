from rest_framework import serializers
from .models import Image


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image  # 指定的模型类
        fields = ('__unicode__', 'name','image')  # 需要序列化的属性

