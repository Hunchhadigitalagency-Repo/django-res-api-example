from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Student
      fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
      model = Teacher
      fields = '__all__'
