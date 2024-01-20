from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    # add data
    path('add-student/', postStudent),
    path('add-teacher/', postTeacher),

    # fetch data
    path('get-student/', getStudent),


    # edit data
    path('edit-student/<id>',editStudentData),
    path('update-student/<int:id>',updateStudentData),

    # delete data
    path('delete-student/<int:id>', deleteStudentData),
    
]