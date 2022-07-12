from django.test import TestCase
from django.urls import reverse


class MonitoringUrlsTest(TestCase):
    def test_monitoring_urls_is_correct(self):
        url = reverse('monitoring:home')
        self.assertEqual(url, '/monitoring/')
