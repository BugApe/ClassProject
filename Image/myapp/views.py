from django.shortcuts import render

# Create your views here.

from rest_framework import  mixins,viewsets
from myapp.models import Image
from myapp.serializers import ImageSerializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



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

        #在此处调用算法
        #headers = self.get_success_headers(serializer.data)
        name_re_photo = serializer.data['name']  # 提取字段name
        #object_worker = worker.objects.filter(name=name_re_photo)  # 从worker中查询是否匹配name_re_photo
        if len(name_re_photo) != 0:  # 研究是否有匹配的name
            #serializer2 = WorkerSerializer(object_worker, many=True)
            #serializer2.data[0]['photo'] = 'http://127.0.0.1:8000/api/recognition/' + serializer2.data[0]['photo']
           result = 0
               #test.getresult(36)  # 人脸识别函数，先构造简单函数替代


        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Working right.',
            "tag": 'pass',
            #"data": serializer2.data
        }
        )  # 返回worker中匹配的图片地址




    def post(self, request):
        return self.create(request)

    def post(self, request):
        return self.create(request)

