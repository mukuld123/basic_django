from django.urls import path
from . import views
from .views import EmpListView, EmpDetailView, EmpCreateView, EmpUpdateView, EmpDeleteView

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('all_emp/', EmpListView.as_view(), name='all_employees'),
    path('emp/<int:pk>/', EmpDetailView.as_view(), name='details'),
    path('emp/new/', EmpCreateView.as_view(), name='create'),
    path('emp/<int:pk>/update', EmpUpdateView.as_view(), name='update'),
    path('emp/<int:pk>/delete', EmpDeleteView.as_view(), name='delete'),
]