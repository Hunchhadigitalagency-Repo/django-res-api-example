from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['POST'])
def postStudent(request):
   try:
    request_data = request.data
    serializer_std = StudentSerializer(data=request_data,many = False)
    if serializer_std.is_valid(raise_exception=True):
        serializer_std.save()
        return Response({'message':"student added successfully"})
   except Exception as e:
      return Response({"err":e})



@api_view(['POST'])
def postTeacher(request):
   try:
    request_data = request.data
    serializer_tch = TeacherSerializer(data=request_data,many = False)
    if serializer_tch.is_valid(raise_exception=True):
        serializer_tch.save()
        return Response({'message':"Teacher added successfully"})
   except Exception as e:
      return Response({"err":e})

@api_view(['GET'])
def getStudent(request):
   try:
      students = Student.objects.all()
      serialized_data = StudentSerializer(students, many=True)
      return Response(serialized_data.data)
   except Exception as e:
      return Response({"err":e})   
   
@api_view(['GET'])
def editStudentData(request, id):
   student = Student.objects.get(id=id)
   serialized_data = StudentSerializer(student,many = False)
   return Response(serialized_data.data)

@api_view(['POST'])
def updateStudentData(request, id):
   try:
      student = Student.objects.get(id=id)
      serialized_data = StudentSerializer(student,many = False,data=request.data,partial=True)
      if serialized_data.is_valid(raise_exception=True):
         serialized_data.save()
         return Response({"message":"data updated successfully",
                          "data":serialized_data.data})
   except Exception as e:
      return Response({"err":e})  

@api_view(['GET'])
def deleteStudentData(request,id):
   student = Student.objects.get(id=id)
   student.delete()
   return Response({"message":'Student Data Deleted Successfully'}) 