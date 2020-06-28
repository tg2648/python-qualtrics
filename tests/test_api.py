# Standard library imports
import datetime
import json
import unittest

# Third party imports
import responses

# Local imports
from qualtrics import api


def suite():
    pass


class ApiTestCase(unittest.TestCase):
    def test_init_sets_config(self):
        client = api.QualtricsAPI(
            data_center='ab1',
            api_key='abcd1234#$%'
        )
        self.assertEqual(client.config.get('data_center'), 'ab1')
        self.assertEqual(client.config.get('api_key'), 'abcd1234#$%')
        self.assertEqual(client.config.get('base_url'), 'https://ab1.qualtrics.com/API/v3/')
