from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields = ('company_logo','company_name','about','company_email','company_tel_number','company_reg_number','joined_on')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user