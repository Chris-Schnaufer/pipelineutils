"""Test cases for the Clowder interface
"""

import os
import unittest

import pipelineutils.pipelineutils.pipelineutils as pu

USERNAME = "test@example.com"
PASSWORD = "testPassword"

CLOWDER_URI = os.getenv("CLOWDER_HOST_URI", "http://localhost:9000")

class ClowderTestCase(unittest.TestCase):
    """Testing the clowder connections
    """
    
    def setup(self):
        """Test preparation for every unit test
        """
        # Nothing to setup
    
    def teardown(self):
        """Test cleanup for every unit test
        """
        # Nothing to tear down
        
    def test_get_api_key(self):
        """Unit test for getting an API key from Clowder
        """
        a_key = None
        try:
            a_key = pu.__local__.get_api_key(CLOWDER_URI, USERNAME, PASSWORD)
        except Exception as ex:
            print("Exception was caught: ", str(ex))
        finally:
            self.assertNotEqual(a_key, None, "No key was returned from clowder instance")
