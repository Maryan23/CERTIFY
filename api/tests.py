from django.test import TestCase
from .models import Employer
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