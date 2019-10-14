
from django.shortcuts import render

# Create your views here.

from rest_framework import  mixins,viewsets
from myapp.models import Image
from myapp.serializers import ImageSerializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import  Avatar.main as tou


# Create your views here.


class ImageViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = Image.objects.all().order_by('name')
    # 指定序列化的类
    serializer_class = ImageSerializers
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # 对上传的图片序列化
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        name_re_photo = serializer.data['name']  # 提取字段name

        tou.main()
        #去掉文件名的后缀
        index=name_re_photo.rindex('.')
        name_re_photo=name_re_photo[:index]
        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Working right.',
            "tag": 'pass',
            "data": 'http://127.0.0.1:8000/static/UGATIT_selfie2anime_lsgan_4resblock_6dis_1_1_10_10_1000_sn_smoothing/'+name_re_photo +'.jpg'
        }
        )  # 返回worker中匹配的图片地址




