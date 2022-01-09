from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import  IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


# from .models import Employer
# from .serializers import EmployerSerializer

# Create your views here.
# class EmployerList(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get(self,request,format=None):
#         employers = Employer.objects.all()
#         serializer = EmployerSerializer(employers,many=True)
#         return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
