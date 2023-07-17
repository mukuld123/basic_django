from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from employeeApp.models import Employee

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
