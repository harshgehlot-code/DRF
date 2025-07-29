from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# model object - single student data

def student_info(request, pk):
    # Fetching a single student object from the database
    stu = Student.objects.get(id = pk)
   
    # Serializing the model object
    # Using the StudentSerializer to convert the model instance into a format suitable for JSON rendering
    serializer = StudentSerializer(stu) 
   
    # Converting the serialized data to JSON format
    # JSONRenderer is used to render the serialized data into JSON format
    # json_data  = JSONRenderer().render(serializer.data)

    # # Returning the JSON response to the client
    # return HttpResponse(json_data, content_type='application/json')

    # Returning the serialized data as a JsonResponse
    # JsonResponse is a Django utility that converts the data to JSON format and sets the appropriate
    return JsonResponse(serializer.data, safe=False)

def student_list(request):
    # Fetching a single student object from the database
    # This retrieves all student objects from the database
    # The Student model is assumed to be defined in models.py
    stu = Student.objects.all()
   
    # Serializing the model object
    # Using the StudentSerializer to convert the model instance into a format suitable for JSON rendering
    # Here, many=True indicates that we are serializing a queryset (multiple objects)
    serializer = StudentSerializer(stu, many=True) 
   
    # Converting the serialized data to JSON format
    # JSONRenderer is used to render the serialized data into JSON format
    # json_data  = JSONRenderer().render(serializer.data)

    # Returning the JSON response to the client
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)