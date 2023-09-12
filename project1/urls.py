"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appi.views import *

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('manager',ManagerViewSet,basename='man')
router.register('managermodel',MamagerModelViewSet,basename='manager')
router.register('user',SignupViewset,basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp',EmpView.as_view()),
    path('empspec/<int:id>',EmployeeSpecView.as_view()),
    path('manager',ManagerView.as_view()),
    path('manspec/<int:id>',ManagerSpecificView.as_view()),
    path('employee',EmployeeView.as_view()),
    path('employeespec/<int:id>',EmployeeSpecView.as_view()),
    path('man',ManagerView.as_view()),
    path('man/<int:id>',ManagerSpecView.as_view())
]+router.urls
