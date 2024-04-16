import unittest
from unittest.mock import patch, MagicMock
import json
import urllib.request
import main
from main import get_models_for_make, get_all_models

"""
Test Script get_all_models function
"""

"""
class TestGetModelsForMake(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_get_models_for_make(self, mock_urlopen):
        # Define the expected JSON response data
        expected_data = {'Results': [{'Make_ID': 475, 'Make_Name': 'Acura', 'Model_ID': 1867, 'Model_Name': 'ZDX'}]}

        # Create a MagicMock object to mimic the response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(expected_data).encode('utf-8')

        # Patch urlopen to return the mock response
        mock_urlopen.return_value = mock_response

        # Call the function under test
        result = get_models_for_make('acura')

        # Assert the result
        self.assertEqual(result, expected_data.get('Results', []))

        
        #mock_response = MagicMock()
        #mock_response.read.return_value.decode.return_value = '{"Results": [{"Make_ID": 1, "Make_Name": "Acura", ' \
                                                     #         '"Model_ID": 1, "Model_Name": "MDX"}]}'
        #mock_urlopen.return_value = mock_response
        # Call the function
        #result = get_models_for_make('acura')
        # Assert expected result
        #expected_result = [{'Make_ID': 1, 'Make_Name': 'Acura', 'Model_ID': 1, 'Model_Name': 'MDX'}]
        #self.assertEqual(result, expected_result)
        
"""


class TestGetAllModels(unittest.TestCase):

    @patch('main.get_models_for_make')
    def test_get_all_models(self, mock_get_models_for_make):
        # Mock get_models_for_make function and pass it in ^ as the list
        mock_get_models_for_make.side_effect = [
            [{'Make_ID': 1, 'Make_Name': 'Acura', 'Model_ID': 1, 'Model_Name': 'MDX'}],
            [{'Make_ID': 2, 'Make_Name': 'Honda', 'Model_ID': 2, 'Model_Name': 'Civic'}],
            [{'Make_ID': 3, 'Make_Name': 'Chevrolet', 'Model_ID': 3, 'Model_Name': 'Silverado'}],
            [{'Make_ID': 4, 'Make_Name': 'Toyota', 'Model_ID': 4, 'Model_Name': 'Camry'}],
            [{'Make_ID': 5, 'Make_Name': 'Ford', 'Model_ID': 5, 'Model_Name': 'F-150'}]
        ]
        # Call the function
        result = get_all_models()
        # Make an expected result
        expected_result = [
            {'Make_ID': 1, 'Make_Name': 'Acura', 'Model_ID': 1, 'Model_Name': 'MDX'},
            {'Make_ID': 2, 'Make_Name': 'Honda', 'Model_ID': 2, 'Model_Name': 'Civic'},
            {'Make_ID': 3, 'Make_Name': 'Chevrolet', 'Model_ID': 3, 'Model_Name': 'Silverado'},
            {'Make_ID': 4, 'Make_Name': 'Toyota', 'Model_ID': 4, 'Model_Name': 'Camry'},
            {'Make_ID': 5, 'Make_Name': 'Ford', 'Model_ID': 5, 'Model_Name': 'F-150'}
        ]
        self.assertEqual(result, expected_result)

    # Test for get all models with an extra make to filter out
    @patch('main.get_models_for_make')
    def test_get_all_models_filter_extra_make(self, mock_get_models_for_make):
        mock_get_models_for_make.side_effect = [
            [{'Make_ID': 1, 'Make_Name': 'Acura', 'Model_ID': 1, 'Model_Name': 'MDX'}],
            [{'Make_ID': 2, 'Make_Name': 'Honda', 'Model_ID': 2, 'Model_Name': 'Civic'}],
            [{'Make_ID': 3, 'Make_Name': 'Chevrolet', 'Model_ID': 3, 'Model_Name': 'Silverado'}],
            [{'Make_ID': 4, 'Make_Name': 'Toyota', 'Model_ID': 4, 'Model_Name': 'Camry'}],
            [{'Make_ID': 5, 'Make_Name': 'Ford', 'Model_ID': 5, 'Model_Name': 'F-150'}],
            [{'Make_ID': 6, 'Make_Name': 'Lexus', 'Model_ID': 6, 'Model_Name': 'Optima'}]
        ]
        result = get_all_models()
        expected_result = [
            {'Make_ID': 1, 'Make_Name': 'Acura', 'Model_ID': 1, 'Model_Name': 'MDX'},
            {'Make_ID': 2, 'Make_Name': 'Honda', 'Model_ID': 2, 'Model_Name': 'Civic'},
            {'Make_ID': 3, 'Make_Name': 'Chevrolet', 'Model_ID': 3, 'Model_Name': 'Silverado'},
            {'Make_ID': 4, 'Make_Name': 'Toyota', 'Model_ID': 4, 'Model_Name': 'Camry'},
            {'Make_ID': 5, 'Make_Name': 'Ford', 'Model_ID': 5, 'Model_Name': 'F-150'}
        ]
        self.assertEqual(result, expected_result)

    # Test for get all models with empty list
    @patch('main.get_models_for_make')
    def test_get_all_models_empty_response(self, mock_get_models_for_make):
        # Mock an empty list
        mock_get_models_for_make.return_value = []
        # Call the function under test
        result = main.get_all_models()
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()

"""
class TestMain(unittest.TestCase):

    @patch('main.urllib.request.urlopen')
    def test_get_models_for_make(self, mock_urlopen):
        # Mock the response from the NHTSA API
        mock_response = {'Results': [{'Make_ID': 1, 'Make_Name': 'Acura', 'Model_ID': 1, 'Model_Name': 'MDX'}]}
        mock_urlopen.return_value.read.return_value.decode.return_value = json.dumps(mock_response)

        # Test the function with a specific make
        models = get_models_for_make('acura')
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0]['Make_Name'], 'Acura')

    def test_get_all_models(self):
        # Test the get_all_models function
        all_models = get_all_models()
        self.assertTrue(all_models)
        self.assertTrue(len(all_models) > 0)



if __name__ == '__main__':
    unittest.main()
    """
