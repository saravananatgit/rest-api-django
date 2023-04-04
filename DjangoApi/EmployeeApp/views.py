from math import fabs
from urllib import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from EmployeeApp.models import Departments, Employess
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Added Succesfully', safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        #print('pringint data....', department_data['DepartmentId'])
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("updated successfully", safe=False)
        return JsonResponse('Update Failed')
    elif request.method=='DELETE':
        print('selected ID==', id)
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


 
@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employess.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data=JSONParser().parse(request)
        print('employee_data', employee_data)
        employee_serializer = EmployeeSerializer(data=employee_data)
        print('employee_data is valid', employee_serializer.is_valid())
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employess.objects.get(EmployeeId = employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Updated Successfully', safe=False)
        return JsonResponse('Update Failed', safe=False)
    elif request.method == 'DELETE':
        employee = Employess.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@csrf_exempt
def SaveFile(request):
    
    file = request.FILES['uploadFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

