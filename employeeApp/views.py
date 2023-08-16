from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Django_EMS.serializers import EmployeeSerializer
from employeeApp.models import Employee
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Generic_views
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# concrete_view_class
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# ViewSet
from rest_framework import status
from rest_framework import viewsets

# authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def HomePage(request):
    return render(request, 'index.html')


# def all_employees(request):
#     context = {
#         'employees' : Employee.objects.all()
#     }
#     # print(context)
#     return render(request, 'all_employees.html', context)

class EmpListView(ListView):
    model = Employee
    template_name = 'all_employees.html'
    context_object_name = 'employees'
    ordering = ['joining_date']

class EmpDetailView(DetailView):
    model =  Employee
    template_name = 'emp_details.html'
    context_object_name = 'employees'

class EmpCreateView(CreateView):
    model = Employee
    template_name = 'emp_form.html'
    fields = ['firstName', 'lastName', 'dept', 'role', 'phone', 'joining_date', 'location']

class EmpUpdateView(UpdateView):
    model = Employee
    template_name = 'emp_form.html'
    fields = ['firstName', 'lastName', 'dept', 'role', 'phone', 'joining_date', 'location']

class EmpDeleteView(DeleteView):
    model = Employee
    template_name = 'emp_confirm_delete.html'
    fields = ['firstName', 'lastName', 'dept', 'role', 'phone', 'joining_date', 'location']
    success_url = '/'


def emp_details(request, pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(emp)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def emp_list(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


#  Browsable API
@api_view(['GET','POST'])    
def get_emp_details(request):
    if request.method == 'GET':
        return Response({'msg':'GET request is sent'})
    
    # print(request.data)
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("Yo")
        return Response({'msg':'POST request is sent', 'data':request.data})
    else:
        return Response({'msg':'POST request is NOT sent'})
    

class EmployeeAPI(APIView):
    def get(self, request, format = None):
        return Response({'msg':'GET request is sent'})
    
    def post(self, request,format = None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Yo")
            return Response({'msg':'POST request is sent', 'data': serializer.data})
        else:
            return Response({'msg':'POST request is NOT sent'})
        

class LCGenericAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RUDGenericAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
# concrete view class
class EmployeeListCreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# viewSet
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        id = pk
        emp = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg':'Data deleted'})
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
