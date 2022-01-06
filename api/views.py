from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Institution, Learner
from .serializer import InstitutionSerializer, LearnerSerializer

# Create your views here.
class InstitutionList(APIView):
  def get(self, request, format=None):
    all_institutions = Institution.objects.all()
    serializers=InstitutionSerializer(all_institutions, many=True)
    return Response(serializers.data)
  
class LearnerList(APIView):
  def get(self, request, format=None):
    all_learners = Learner.objects.all()
    serializers = LearnerSerializer(all_learners, many=True)
    return Response(serializers.data)
  
  def post(self, request, format=None):
    serializers = LearnerSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
from .serializer import EmployerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import  IsAdminOrReadOnly
from .models import Employer

# Create your views here.
class EmployerList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        employers = Employer.objects.all()
        serializer = EmployerSerializer(employers,many=True)
        return Response(serializer.data)
