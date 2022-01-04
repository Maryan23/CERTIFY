from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
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
