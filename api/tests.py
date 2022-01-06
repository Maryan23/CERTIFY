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
    
  # Test delete institution
  def test_delete_institution(self):
    self.institution.save_institution()
    self.institution.delete_institution()
    saved_institutions = Institution.objects.all()
    self.assertTrue(len(saved_institutions)==0)
    
class LearnerTestCase(TestCase):
  # Set up method
  def setUp(self):
    # Create an institution instance
    self.institution = Institution(institution_reg_no = 'smmq/00124/2016', institution_name = 'Phoenix Developers',institution_email = 'contact@phoenixdevelopers.com', location_name = 'Upper Hill', location_address = '053-100 Nairobi')
    self.institution.save_institution()
    # Create a learner instance.
    self.learner = Learner(learner_reg_no = 'smp/1234/2021', learner_first_name='kelvin', learner_second_name='Kevson', learner_last_name='Kimani', course_taken='Full Stack Development', date_enrolled='2021-07-12', date_completed='2021-12-12',grade_attained='Distinction', certificate_image='my-certificate')
    # self.learner.institution.set(self.institution)
    self.learner.save_learner()
    
  # Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.learner, Learner))
    
  # Test save learner
  def test_save_learner(self):
    self.learner.save_learner()
    saved_learners = Learner.objects.all()
    self.assertTrue(len(saved_learners)==1)
    
  def test_delete_learner(self):
    self.learner.save_learner()
    self.learner.delete_learner()
    saved_learners = Learner.objects.all()
    self.assertTrue(len(saved_learners)==0)
    
  # def test_view_learners_by_institution(self):
  #   self.learner.save_learner()
  #   self.learner2 = Learner(learner_reg_no = 'smp/12345/2021', learner_first_name='Martin', learner_second_name='Okelo', learner_last_name='Otieno', course_taken='Full Stack Development', date_enrolled='2021-07-12', date_completed='2021-12-12',grade_attained='Distinction', certificate_image='my-certificate2', institution = self.institution)
  #   self.learner2.save_learner()
  #   saved_learners = Learner.view_learners_by_institution()
  #   self.assertTrue(len(saved_learners)==2)
    