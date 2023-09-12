from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

class EmpView(APIView):
    # def get(self,request,*args,**kwargs):
        # if 'dept' in request.query_params:
        #     dep=request.query_params.get("dept")
        #     res=[i for i in employee if i['dept']==dep]
        #     if 'limit' in request.query_params:
        #         lm=request.query_params.get("limit")
        #         data=res[0:int(lm)]
        #         return Response(data=data)
        #     return Response(data=res)
        # if 'limit' in request.query_params:
        #     lm=request.query_params.get('limit')
        #     data=employee[0:int(lm)]
        #     return Response(data=data)
        # return Response(data=employee)
    def get(self,request,*args,**kwargs):
        emp=employee
        if 'dept' in request.query_params:
            dep=request.quer_params.get("dept")
            emp=[i for i in emp if i['dept']==dep]
        if 'limit' in request.query_params:
            lm=request.query_params.get("limit")
            emp=emp[0:int(lm)]
        return Response(data=emp)

    
    def post(self,request):
        data=request.data
        employee.append(data)
        return Response(data=employee)
    

class EmpSpecificView(APIView):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        # res={}
        # for i in employee:
        #     if i["id"]==eid:
        #         res=i
        res=[i for i in employee if i["id"] == eid].pop()
        return Response(data=res)
    
    def delete(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        res=[i for i in employee if i["id"] == eid].pop()
        employee.remove(res)
        return Response(data=employee)
    
    def put(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        data=request.data
        res=[i for i in employee if i["id"] == eid].pop()
        res.update(data)
        return Response(data=employee)


# MANAGER
class ManagerView(APIView):
    def get(self,request,*args,**kwargs):
        temp=manager
        if 'exp_gt' in request.query_params:
            lm=request.quer_params.get("exp_gt")
            temp=[i for i in manager if i['exp'] > int(lm)]
        return Response(data=temp)
    
    def post(self,request):
        data=request.data
        manager.append(data)
        return Response(data=manager)
    

class ManagerSpecificView(APIView):
    def get(self,request,*args,**kwargs):
        mid=kwargs.get("id")
        res=[i for i in manager if i["id"] == mid]
        return Response(data=res)
    
    def delete(self,request,*args,**kwargs):
        mid=kwargs.get("id")
        res=[i for i in manager if i["id"] == mid].pop()
        manager.remove(res)
        return Response(data=manager)
    
    def put(self,request,*args,**kwargs):
        mid=kwargs.get("id")
        data=request.data
        res=[i for i in manager if i["id"] == mid].pop()
        res.update(data)
        return Response(data=manager)
    
class EmployeeView(APIView):
    def post(self,request):
        ser=EmpSer(data=request.data)
        if ser.is_valid():
            nm=ser.validated_data.get('name')
            dp=ser.validated_data.get('dept')
            ph=ser.validated_data.get('phone')
            Employee.objects.create(name=nm,dept=dp,phone=ph)
            return Response({"msg":"Created"})
        return Response({"msg":"invalid data"}) 
    
    def get(self,request):
        emp=Employee.objects.all()
        dser=EmpSer(emp,many=True)
        return Response(data=dser.data)
    
class EmployeeSpecView(APIView):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        res=Employee.objects.get(id=eid)
        dser=EmpSer(res)
        return Response(data=dser.data)
    
    def delete(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        # res=Employee.objects.get(id=eid)
        # res.delete()
        Employee.objects.filter(id=eid).delete()
        return Response({"msg":"deleted"})
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        emp=Employee.objects.get(id=id)
        ser=EmpSer(data=request.data)
        if ser.is_valid():
            nm=ser.validated_data.get('name')
            dp=ser.validated_data.get('dept')
            ph=ser.validated_data.get('phone')
            emp.name=nm
            emp.dept=dp
            emp.phone=ph
            emp.save()
            return Response({"msg":"updated"})
        return Response({"msg":ser.errors})
    
from rest_framework import status
class ManagerView(APIView):
    def post(self,request):
        # try:
            ser=ManagerModelSer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"created"})
            return Response({"msg":"failed"})
        # except:
            # return Response({"msg":"Error"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def get(self,request):
        man=Manager.objects.all()
        if 'exp_gt' in request.query_params:
            exp=request.query_params.get('exp_gt')
            man=man.filter(experience__gt=exp)
        if 'limit' in request.query_params:
            lm=request.query_params.get('limit')
            man=man[0:int(lm)]
        dser=ManagerModelSer(man,many=True)
        return Response(data=dser.data)

    

class ManagerSpecView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            mid=kwargs.get("id")
            man=Manager.objects.get(id=mid)
            dser=ManagerModelSer(man)
            return Response(data=dser.data)
        except:
            return Response({"msg":"Error"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def delete(self,request,**kwargs):
        try:
            mid=kwargs.get("id")
            man=Manager.objects.get(id=mid)
            man.delete()
            return Response({"msg":"deleted"})
        except:
            return Response({"msg":"Error"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
    def put(self,request,**kwargs):

        try:
            mid=kwargs.get("id")
            man=Manager.objects.get(id=mid)
            ser=ManagerModelSer(data=request.data,instance=man)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"updated"})
            return Response({"msg":"failed"})
        except:
            return Response({"msg":"Error"},status=status.HTTP_406_NOT_ACCEPTABLE)
        

from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions

class ManagerViewSet(ViewSet):
    def retrieve(self,request,*args,**kwargs):
        mid=kwargs.get('pk')
        man=Manager.objects.get(id=mid)
        dser=ManagerModelSer(man)
        return Response(data=dser.data)
    def list(self,request,*args,**kwargs):
        man=Manager.objects.all()
        dser=ManagerModelSer(man,many=True)
        return Response(data=dser.data)
    def create(self,request):
        ser=ManagerModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"},status=status.HTTP_201_CREATED)
        return Response({"msg":"failed"},status=status.HTTP_404_NOT_FOUND)
    def update(self,request,*args,**kwargs):
        mid=kwargs.get('pk')
        man=Manager.objects.get(id=mid)
        ser=ManagerModelSer(data=request.data,instance=man)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        return Response({"msg":"failed"})
    
    def destroy(self,request,**kwargs):
        mid=kwargs.get('pk')
        man=Manager.objects.get(id=mid)
        man.delete()
        return Response({"msg":"Deleted"})
        
class MamagerModelViewSet(ModelViewSet):
    serializer_class=ManagerModelSer
    queryset=Manager.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]


class SignupViewset(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=UserModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"User Created"})
        return Response({"msg":"failed"})
