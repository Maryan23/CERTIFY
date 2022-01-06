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
