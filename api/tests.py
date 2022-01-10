from django.test import TestCase
from .models import Employer,Institution,Learner
from django.contrib.auth.models import User


class EmployerTestClass(TestCase):
    #Set Up method
    def setUp(self):
        self.teloperators = Employer(company_logo = 'image.png',company_name='Teloperators',about = 'We love phones',company_tel_number = '0712345678',company_email='teloperators@test.com',company_reg_number='B2345')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.teloperators,Employer))

    # Testing Save Method
    def test_save_method(self):
        self.teloperators.save_employer()
        employers = Employer.objects.all()
        self.assertTrue(len(employers) > 0)

    def tearDown(self):
        Employer.objects.all().delete()

    # Testing Update Method
    def test_update_method(self):
        self.teloperators.update_employer()
        employers = Employer.objects.all()
        self.assertTrue(len(employers) > 0)

    def test_search_by_company_name(self):
        user = 1
        employer = Employer.search_by_company_name(user)
        self.assertFalse(len(employer)>0)

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