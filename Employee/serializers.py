from rest_framework import serializers
from .models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False,read_only=True)

    class Meta:
        model = Employee
        fields = ['id','name','email','mobile','department']

class AddEmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(required=True)

    class Meta:
        model = Employee
        fields = ['id','name','email','mobile','department']        