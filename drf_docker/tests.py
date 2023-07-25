from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import EmployeeProfile

class EmployeeProfileTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_employee = EmployeeProfile.objects.create(
            owner=testuser1,
            full_name="John Doe",
            date_of_birth="1990-01-01",
            position="Software Engineer",
            outside_contractor=False
        )

    def test_employee_profile_model(self):
        employee = EmployeeProfile.objects.get(id=1)
        actual_owner = str(employee.owner)
        actual_full_name = str(employee.full_name)
        actual_date_of_birth = str(employee.date_of_birth)
        actual_position = str(employee.position)
        actual_outside_contractor = employee.outside_contractor

        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_full_name, "John Doe")
        self.assertEqual(actual_date_of_birth, "1990-01-01")
        self.assertEqual(actual_position, "Software Engineer")
        self.assertFalse(actual_outside_contractor)

    def test_contractor_employee_profile_model(self):
        testuser2 = get_user_model().objects.create_user(username='testuser2', password='pass')
        testuser2.save()

        test_contractor_employee = EmployeeProfile.objects.create(
            owner=testuser2,
            full_name="Jane Smith",
            date_of_birth="1985-05-15",
            position="Contractor",
            outside_contractor=True
        )

        contractor_employee = EmployeeProfile.objects.get(id=2)
        actual_owner = str(contractor_employee.owner)
        actual_full_name = str(contractor_employee.full_name)
        actual_date_of_birth = str(contractor_employee.date_of_birth)
        actual_position = str(contractor_employee.position)
        actual_outside_contractor = contractor_employee.outside_contractor

        self.assertEqual(actual_owner, str(testuser2))
        self.assertEqual(actual_full_name, "Jane Smith")
        self.assertEqual(actual_date_of_birth, "1985-05-15")
        self.assertEqual(actual_position, "Contractor")
        self.assertTrue(actual_outside_contractor)
