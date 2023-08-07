from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    def create(self):
        student = Student(
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            email=self.validated_data.get('email'),
            mobile_number=self.validated_data.get('mobile_number'),
            rollno=self.validated_data.get('rollno'),
            admission_date=self.validated_data.get('admission_date')
        )
        student.save()
        return student
    def update(self,student):
        student.first_name=self.validated_data.get('first_name')
        student.last_name=self.validated_data.get('last_name')
        student.email=self.validated_data.get('email')
        student.mobile_number=self.validated_data.get('mobile_number')
        student.rollno=self.validated_data.get('rollno')
        student.admission_date=self.validated_data.get('admission_date')
        student.save()
        return student    

    class Meta:
        model = Student
        fields = '__all__'
