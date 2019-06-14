from django.test import TestCase
from  django.urls import reverse
# Create your tests here.
class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		repsonse =self.client.get(url)
		self.assertEquals(repsonse.status_code, 200)