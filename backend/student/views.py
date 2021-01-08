from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from .models import Students
from rest_framework.views import APIView 
from .serializers import StudentSerializer
from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse

class StudentView(APIView): 
    
    serializer_class = StudentSerializer
    global stud 
    stud= [ {"Roll": detail.Roll,"Name":detail.Name,"Maths":detail.Maths,"Physics":detail.Physics,
        "Chemistry":detail.Chemistry,"Total":detail.Total,"Percentage":detail.Percentage}  
        for detail in Students.objects.all()] 
    def get(self, request): 
        return JsonResponse(stud,safe=False) 
  
    def post(self, request): 
  
        serializer = StudentSerializer(data=request.data) 
        
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            data=stud.append(serializer.data)
            return  Response(stud) 
    