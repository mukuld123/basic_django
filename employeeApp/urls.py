from django.urls import path, include
from . import views
from .views import EmpListView, EmpDetailView, EmpCreateView, EmpUpdateView, EmpDeleteView
from .views import EmployeeAPI
from employeeApp import views
from .views import LCGenericAPI, RUDGenericAPI
from .views import EmployeeListCreate, EmployeeReadUpdateDelete

# viewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employeeapi', views.EmployeeViewSet, basename='employee')

# modelViewSet
router.register('employeeapi_2', views.EmployeeViewSet, basename='employee')


urlpatterns = [
    # path('', views.HomePage, name='homepage'),
    path('all_emp/', EmpListView.as_view(), name='all_employees'),
    path('emp/<int:pk>/', EmpDetailView.as_view(), name='details'),
    path('emp/new/', EmpCreateView.as_view(), name='create'),
    path('emp/<int:pk>/update', EmpUpdateView.as_view(), name='update'),
    path('emp/<int:pk>/delete', EmpDeleteView.as_view(), name='delete'),

    path('emp_details/<int:pk>', views.emp_details),
    path('emp_details/', views.emp_list),

    path('get_emp_details/', views.get_emp_details),
    path('get_emp_details_2/', EmployeeAPI.as_view()),

    path('generic_details/', LCGenericAPI.as_view()),
    path('generic_details/<int:pk>/', RUDGenericAPI.as_view()),

    path('concrete_view/', EmployeeListCreate.as_view()),
    path('concrete_view/<int:pk>/', EmployeeReadUpdateDelete.as_view()),

    # viewSet
    path('', include(router.urls)),



]