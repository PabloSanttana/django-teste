from django.test import TestCase
from django.urls import reverse, resolve

from monitoring import views


class MonitoringUrlsTest(TestCase):
    def test_monitoring_home_view_function_is_correct(self):
        url = reverse('monitoring:home')
        view = resolve(url)
        view = self.assertIs(view.func, views.home)

    def test_monitoring_home_view_returns_status_200_ok(self):
        url = reverse('monitoring:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_monitoring_home_view_loads_correct_template(self):
        url = reverse('monitoring:home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'monitoring/pages/home.html')
