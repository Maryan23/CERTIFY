from rest_framework import serializers
from .models import Institution, Learner

class InstitutionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Institution
    fields = ('institution_reg_no', 'institution_name', 'location_name', 'location_address', 'institution_email')
    
class LearnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Learner
    fields = ('learner_reg_no', 'learner_first_name', 'learner_second_name', 'learner_last_name', 'course_taken', 'date_enrolled', 'date_completed', 'grade_attained', 'certificate_image', 'institution')
    
    