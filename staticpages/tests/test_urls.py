#!/usr/bin/env python

import os

from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.core.urlresolvers import reverse

class URLTest(TestCase):
    urls = 'staticpages.tests.urls'
    def setUp(self):
        self.c = Client()
        settings.STATICPAGES_TEMPLATES = [
            ('homesite', os.path.join(os.path.dirname(__file__), 'my_static_site'))
        ]

    def tearDown(self):
        del self.c

    def test_basic_functionality(self):
        response = self.c.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('about' in response.content)

    def test_index(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('index' in response.content)
    
    def test_index_name(self):
        self.assertEqual(reverse('homesite_index'), '/')
    
    def test_name(self):
        self.assertEqual(reverse('homesite_about'), '/about/')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
