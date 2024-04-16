import json
import unittest
from unittest.mock import patch

import GrabHondaVehicleIds


class TestGetVehicleIdsForModelYear(unittest.TestCase):

    @patch('main.urllib.request.urlopen')
    def test_get_vehicle_ids_for_model_year(self, mock_urlopen):
        mock_response = {
            'Results': [{'VehicleId': '1'}, {'VehicleId': '2'}, {'VehicleId': '3'}]
        }
        mock_urlopen.return_value.__enter__.return_value.read.return_value.decode.return_value = json.dumps(mock_response)

        make = 'acura'
        model = 'mdx'
        year = 2020

        expected_result = ['1', '2', '3']
        result = GrabHondaVehicleIds.get_vehicle_ids_for_model_year(make, model, year)

        self.assertEqual(result, expected_result)


class TestAggregateVehicleIds(unittest.TestCase):

    @patch('GrabHondaVehicleIds.get_vehicle_ids_for_model_year')
    def test_aggregate_vehicle_ids(self, mock_get_vehicle_ids_for_model_year):
        # Input data
        models = [
            {"Make_ID": 475, "Make_Name": "Acura", "Model_ID": 1867, "Model_Name": "ZDX"},
            {"Make_ID": 475, "Make_Name": "Acura", "Model_ID": 1871, "Model_Name": "RDX"}
            # Add more models if needed
        ]
        start_year = 2022
        end_year = 2023
        # Mock return values for get_vehicle_ids_for_model_year
        mock_get_vehicle_ids_for_model_year.side_effect = [
            [],  # Return value for the first call
            [14143, 14142],  # Return value for the second call
            [15144, 15142],  # Return value for the third call
            [16838, 16837]  # Return value for the fourth call
            # Add more return values if needed
        ]
        # Call the function under test
        result = GrabHondaVehicleIds.aggregate_vehicle_ids(models, start_year, end_year)

        # Expected result
        expected_result = {
            "ZDX": {"2022": [], "2023": [14143, 14142]},
            "RDX": {"2022": [15144, 15142], "2023": [16838, 16837]}
        }
        # Assertions
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
