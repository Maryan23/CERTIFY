from django.contrib.auth.models import User
# from django.contrib.auth.models import Permission
from rest_framework import serializers, viewsets

from .models import Institution, Learner
from django.contrib.auth import get_user_model

User = get_user_model()

# class PermissionViewSet(viewsets.ModelViewSet):
#   model = Permission

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password', 'groups')
    extra_kwargs = {'password' : {'write_only':True, 'required':True}}
    
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user

class InstitutionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Institution
    fields = ('institution_reg_no', 'institution_name', 'location_name', 'location_address', 'institution_email')
    
class LearnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Learner
    fields = ('learner_reg_no', 'learner_first_name', 'learner_second_name', 'learner_last_name', 'course_taken', 'date_enrolled', 'date_completed', 'grade_attained', 'certificate_image', 'institution')
    
    