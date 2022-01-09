from django.http.response import JsonResponse
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Employer
from .serializers import EmployerSerializer
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required




#Create your views here.
@login_required
def EmployerList(request,id=0):
    authentication_classes = (TokenAuthentication)
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        employers = Employer.objects.all()
        employer_serializer = EmployerSerializer(employers,many=True)
        return JsonResponse(employer_serializer.data , safe = False)

    elif request.method == 'POST':
        employer_data = JSONParser().parse(request)
        employer_serializer = EmployerSerializer(data=employer_data)
        if employer_serializer.is_valid():
            employer_serializer.save()
            return JsonResponse('Employer added successfully!')

        return JsonResponse('Employer failed to add!')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
