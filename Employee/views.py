from .models import Employee,Department
from django.shortcuts import get_object_or_404
from Employee.serializers import EmployeeListSerializer,AddEmployeeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class EmployeeViewSet(viewsets.ViewSet):

    def get_queryset(self):
        self.queryset = Employee.objects.all()
        return self.queryset
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = EmployeeListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeListSerializer(user)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = AddEmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Employee added successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)   