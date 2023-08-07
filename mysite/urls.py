from django.contrib import admin
from django.urls import include, path,re_path
from Employee.views import EmployeeViewSet
from student.views import StudentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'students', StudentViewSet, basename='students')
urlpatterns = [
    re_path(r'^api/', include(router.urls)),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]