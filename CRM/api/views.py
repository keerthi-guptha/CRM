from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Enrol
from .serializers import EnrolSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions
from rest_framework import generics
# Create your views here
# .
class EnrolList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Enrol.objects.all()
    serializer_class = EnrolSerializer


class EnrolDetail(generics.RetrieveDestroyAPIView):
    queryset = Enrol.objects.all()
    serializer_class = EnrolSerializer



@api_view(['GET'])
def getRoutes(request):
    data = Enrol.objects.filter(course = 'java')

    #data = Enrol.objects.all()
    s_data = EnrolSerializer(data,many=True)

    return Response(s_data.data)

@api_view(['GET'])
def getPython(request):
    data = Enrol.objects.filter(course = 'python')
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)
@api_view(['GET'])
def getJava(request):
    data = Enrol.objects.filter(course = 'java')
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)
@api_view(['GET'])
def getTesting(request):
    data = Enrol.objects.filter(course = 'testing')
    s_data = EnrolSerializer(data,many=True)
    return Response(s_data.data)


@api_view(['POST'])
def insertData(request):
    student = EnrolSerializer(data = request.data)
    #print(student)
    if student.is_valid():
        student.save()
        return Response(student.data,status = status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data",status = status.HTTP_400_BAD_REQUEST )