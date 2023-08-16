from rest_framework import serializers
from employeeApp.models import Employee

# class EmployeeSerializer(serializers.Serializer):
#     firstName = serializers.CharField(max_length=50)
#     lastName = serializers.CharField(max_length=50)
#     dept = serializers.CharField(max_length=50)
#     role = serializers.CharField(max_length=50)
#     phone = serializers.IntegerField()
#     joining_date = serializers.DateField()
#     location = serializers.CharField(max_length=50)

# alternative
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'firstName', 'lastName', 'dept', 'role', 'joining_date','phone', 'location']
