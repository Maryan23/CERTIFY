from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employer,Institution,Learner
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}


class InstitutionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Institution
    fields = ('institution_reg_no', 'institution_name', 'location_name', 'location_address', 'institution_email')
    
class LearnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Learner
    fields = ('learner_reg_no', 'learner_first_name', 'learner_second_name', 'learner_last_name', 'course_taken', 'date_enrolled', 'date_completed', 'grade_attained', 'certificate_image', 'institution')
    
    
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields = ('company_logo','company_name','about','company_email','company_tel_number','company_reg_number','joined_on')
