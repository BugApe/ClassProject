from rest_framework import serializers
from .models import StyleImage


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = StyleImage  # 指定的模型类
        fields = ('__unicode__', 'name','image','style')  # 需要序列化的属性

