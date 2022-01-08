from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Institution, Learner
from .serializers import InstitutionSerializer, LearnerSerializer, UserSerializer

# Create your views here
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

@csrf_exempt
@login_required
def institutionAPI(request, id=0):
  authentication_classes = (TokenAuthentication,)
  permission_classes = [IsAuthenticated]
  if request.method == 'GET':
    institutions = Institution.objects.all()
    institutions_serializer = InstitutionSerializer(institutions, many = True)
    return JsonResponse(institutions_serializer.data, safe = False)
  
  elif request.method=='POST':
    institution_data = JSONParser().parse(request)
    institution_serializer = InstitutionSerializer(data=institution_data)
    if institution_serializer.is_valid():
      institution_serializer.save()
      return JsonResponse("The add was successfully created", safe=False)
    return JsonResponse("Failed to Add the institution", safe=False)
  
  elif request.method =='PUT':
    institution_data = JSONParser().parse(request)
    institution = Institution.objects.get(institution_reg_no = institution_data['institution_reg_no'])
    institution_serializer=InstitutionSerializer(institution, data = institution_data)
    if institution_serializer.is_valid():
      institution_serializer.save()
      return JsonResponse("Institution data updated successfully", safe=False)
    return JsonResponse("Update Failure", safe=False)
  
  elif request.method=='DELETE':
    institution=Institution.objects.get(id=id)
    institution.delete()
    return JsonResponse("Institution deleted successfully", safe=False)
  
@csrf_exempt
@login_required
def LearnerAPI(request, id=0):
  if request.method == 'GET':
    learners = Learner.objects.all()
    learners_serializer = LearnerSerializer(learners, many = True)
    return JsonResponse(learners_serializer.data, safe = False)
  
  elif request.method=='POST':
    learner_data = JSONParser().parse(request)
    learner_serializer = LearnerSerializer(data=learner_data)
    
    # 37 min https://www.youtube.com/watch?v=1Hc7KlLiU9w
    
    if learner_serializer.is_valid():
      learner_serializer.save()
      return JsonResponse("The add was successfully created", safe=False)
    return JsonResponse("Failed to Add the learner", safe=False)
  
  elif request.method =='PUT':
    learner_data = JSONParser().parse(request)
    learner = Learner.objects.get(learner_reg_no = learner_data['learner_reg_no'])
    learner_serializer=LearnerSerializer(learner, data = learner_data)
    if learner_serializer.is_valid():
      learner_serializer.save()
      return JsonResponse("Learner data updated successfully", safe=False)
    return JsonResponse("Update Failure", safe=False)
  
  elif request.method=='DELETE':
    learner=Learner.objects.get(id=id)
    learner.delete()
    return JsonResponse("Learner deleted successfully", safe=False)