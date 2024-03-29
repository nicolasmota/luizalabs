# coding: utf-8
from __future__ import unicode_literals
from rest_framework import generics
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeList(generics.ListAPIView):

    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

    def paginate_queryset(self, *args, **kwargs):
        # Remove pagination
        return None
