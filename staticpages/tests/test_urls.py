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
        settings.TEMPLATE_DIRS = [
            os.path.join(os.path.dirname(__file__), 'templates')
        ]
        settings.STATICPAGES_TEMPLATES = [
            ('homesite', '', 'my_static_site'),
            ('subsite', 'subsite_url', 'my/sub/site'),
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
        self.assertEqual(reverse('homesite', args=['']), '/')

    def test_name(self):
        self.assertEqual(reverse('homesite', args=['about/']), '/about/')

    def test_subsite_index_name(self):
        self.assertEqual(reverse('subsite', args=['']), '/subsite_url/')

    def test_subsite_name(self):
        self.assertEqual(reverse('subsite', args=['page/']), '/subsite_url/page/')

    def test_subdir_index_name(self):
        self.assertEqual(reverse('homesite', args=['subdir/']), '/subdir/')

    def test_subdir_page_name(self):
        self.assertEqual(reverse('homesite', args=['subdir/subpage/']), '/subdir/subpage/')

    def test_404(self):
        response = self.c.get('/does/not/exist')
        self.assertEqual(response.status_code, 301)
        response = self.c.get('/does/not/exist', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_subsite(self):
        response = self.c.get('/subsite_url/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('subsite' in response.content)

    def test_subsite_page(self):
        response = self.c.get('/subsite_url/page')
        self.assertEqual(response.status_code, 301)
        response = self.c.get('/subsite_url/page', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page' in response.content)

    def test_subdir(self):
        response = self.c.get('/subdir')
        self.assertEqual(response.status_code, 301)
        response = self.c.get('/subdir', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('subdir' in response.content)

    def test_subdir_page(self):
        response = self.c.get('/subdir/subpage')
        self.assertEqual(response.status_code, 301)
        response = self.c.get('/subdir/subpage', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('subpage' in response.content)

    def test_escape(self):
        response = self.c.get('/subsite_url/../inaccessible', follow=True)
        self.assertEqual(response.status_code, 404)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
