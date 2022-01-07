from rest_framework import serializers
from .models import Institution, Learner
class InstitutionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Institution
    fields = ('institution_reg_no', 'institution_name', 'location_name', 'location_address', 'institution_email')
class LearnerSerializer(serializers.ModelSerializer):
  class Meta:
