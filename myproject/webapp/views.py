from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db import connection, models, transaction
from django.http import Http404
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers
from django.utils.encoding import smart_text
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import DefaultSchema
from rest_framework.settings import api_settings
from rest_framework.utils import formatting
from . models import employees
from . serializers import employeesserializers
from django.views.generic import TemplateView

#
def login(request):
    return render(request, 'blog/templates/registration/login.html')


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class employeesList(APIView):

    def get(self,request):
        employees1 = employees.objects.all()
        serializer = employeesserializers(employees1, many=True)
        return Response(serializer.data)

    #
    # def post(self, request):
    #     employees1 = employees.objects.all()
    #     serializer = employeesserializers(employees1, many=True)
    #     if serializer.is_valid(raise_exception=True):
    #         employees_saved = serializer.save()
    #     return Response({"success": "employees '{}' updated successfully".format(employees_saved.temp_id)})
    #
    #
    # def put(self, request, pk):
    #     employees_saved = get_object_or_404(employees.objects.all(), pk=pk)
    #     data = request.data.get('employees')
    #     serializer = employeesserializers(instance=employees_saved, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         employees_saved = serializer.save()
    #     return Response({"success": "employees '{}' updated successfully".format(employees_saved.temp_id)})
    #
    #
    # def delete(self, request, pk):
    #
    #     article = get_object_or_404(employees.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({"message": "employees with id `{}` has been deleted.".format(pk)},status=204)
    

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
