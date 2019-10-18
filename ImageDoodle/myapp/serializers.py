from rest_framework import serializers
from .models import DoodleImage


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoodleImage  # 指定的模型类
        fields = ('__unicode__', 'name','image','style')  # 需要序列化的属性

