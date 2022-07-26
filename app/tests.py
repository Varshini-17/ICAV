# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
# from tastypie.test import ResourceTestCase
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/index')
        self.assertEqual(response.status_code, 200)
    
    def test_endpoint1(self):
        """Test for 1st endpoint"""
        response=self.client.post('http://127.0.0.1:8000/endpoint1', 2)
        self.assertEqual(response.content_type,'application/json')

    def test_endpoint2(self):
        """Test for 2nd endpoint"""
        data = {
            'authors': 'Jesse Grant'
            }
        response = self.client.post(reverse('endpoint2'), data)
        self.assertEqual(response.content_type,'application/json' )

