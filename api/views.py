from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class LearnerstList(APIView):
  def get(self, request, format=None):
    all_learners = Project.objects.all()
    serializers=LearnersSerializer(all_learners, many=True)
    return Response(serializers.data)