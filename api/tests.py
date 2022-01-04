from django.test import TestCase
from .models import Institution, Learner

# Create your tests here.
class InstitutionTestCase(TestCase):
  # Set up method
  def setUp(self):
    self.institution = Institution(institution_reg_no = 'smmq/00124/2016', institution_name = 'Phoenix Developers',institution_email = 'contact@phoenixdevelopers.com', location_name = 'Upper Hill', location_address = '053-100 Nairobi')
    
  # Test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.institution, Institution))
    
  # Test save institution
  def test_save_institution(self):
    self.institution.save_institution()
    saved_institutions = Institution.objects.all()
    self.assertTrue(len(saved_institutions)==1)
    
    
    
    # institution_reg_no = models.CharField(max_length=30)
    # institution_name = models.CharField(max_length=40)
    # location_name = models.CharField(max_length=20)
    # location_address = models.CharField(max_length=20)
    # # institution_email 