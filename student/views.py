from .models import Student
from django.shortcuts import get_object_or_404
from student.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import ValidationError as APIValidationError
from django.core.exceptions import ValidationError
from rest_framework.decorators import action
class StudentViewSet(viewsets.ViewSet):

    def get_student_list_serializer_class(self):
        return StudentSerializer
    
    def list(self, request):
        queryset = Student.objects.all()
        serializer = self.get_student_list_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.get_student_list_serializer_class()(user)
        return Response(serializer.data)
    
    def create(self,request):
        serialized = self.get_student_list_serializer_class()(data = request.data)
        if serialized.is_valid(raise_exception=True):
            student = serialized.create()
            serialized = self.get_student_list_serializer_class()(student)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def update(self,request,pk=None):
        student = Student.objects.filter(pk = pk).first()
        if student:
            serialized = self.get_student_list_serializer_class()(instance=student,data = request.data)
            if serialized.is_valid(raise_exception=True):
                student = serialized.update(student)
                serialized = self.get_student_list_serializer_class()(student)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            raise Http404  
    def destroy(self,request,pk=None):
        student = Student.objects.filter(pk = pk).first()
        if student:
            try:    
                student.delete()
                return Response(data='Deleted successfully')
            except ValidationError as e:
                raise APIValidationError(e.message)
        else:
            raise Http404  

    # @action(methods=['GET'], detail=True)
    # def personal_info(self,request,pk=None):
    #     print("personal_info",pk)
    #     return Response({"message","custom get request personal_info"}, status=status.HTTP_200_OK)

    # @action(methods=['PUT'], detail=True)
    # def update_personal_info(self,request,pk=None):
    #     print(pk)
    #     return Response({"message","custom get request"}, status=status.HTTP_200_OK)    

    # @action(methods=['GET'], detail=True, url_path='personal_info/(?P<employee_id>[-\\w]+)')
    # def update_personal_info(self, request, *args, **kwargs):
    #     print(request.query_params.get("employee_id"))
    #     print(kwargs.get("pk"))
    #     print(kwargs.get("employee_id"))
    #     return Response({"message","custom get request personal_info"}, status=status.HTTP_200_OK)
                      