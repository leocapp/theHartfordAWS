import unittest
from unittest.mock import MagicMock, patch
from SafetyRatingsWVehicleIds import process_vehicle_ids


class TestProcessVehicleIds(unittest.TestCase):

    # Standard test for one year
    @patch('SafetyRatingsWVehicleIds.get_safety_ratings_for_vehicle')
    def test_process_vehicle_ids_single_model_single_year(self, mock_get_safety_ratings_for_vehicle):
        vehicle_ids = {
            'Acura': {
                '2020': [1, 2, 3]
            }
        }
        mock_get_safety_ratings_for_vehicle.side_effect = [
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 1
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 2
            {'safety_rating': 'fair'}  # Safety rating for vehicle ID 3
        ]
        expected_result = {
            'Acura': {
                '2020': {
                    1: {'safety_rating': 'excellent'},
                    2: {'safety_rating': 'good'},
                    3: {'safety_rating': 'fair'}
                }
            }
        }
        result = process_vehicle_ids(vehicle_ids)
        self.assertEqual(result, expected_result)

    # General test for parsing vehicle ids
    @patch('SafetyRatingsWVehicleIds.get_safety_ratings_for_vehicle')
    def test_process_vehicle_ids_multiple_models_multiple_years(self, mock_get_safety_ratings_for_vehicle):
        vehicle_ids = {
            'Acura': {
                '2020': [1, 2],
                '2021': [3, 4]
            },
            'Honda': {
                '2020': [5, 6],
                '2021': [7, 8]
            }
        }
        mock_get_safety_ratings_for_vehicle.side_effect = [
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 1
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 2
            {'safety_rating': 'fair'},  # Safety rating for vehicle ID 3
            {'safety_rating': 'poor'},  # Safety rating for vehicle ID 4
            {'safety_rating': 'average'},  # Safety rating for vehicle ID 5
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 6
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 7
            {'safety_rating': 'fair'}  # Safety rating for vehicle ID 8
        ]
        expected_result = {
            'Acura': {
                '2020': {
                    1: {'safety_rating': 'excellent'},
                    2: {'safety_rating': 'good'}
                },
                '2021': {
                    3: {'safety_rating': 'fair'},
                    4: {'safety_rating': 'poor'}
                }
            },
            'Honda': {
                '2020': {
                    5: {'safety_rating': 'average'},
                    6: {'safety_rating': 'excellent'}
                },
                '2021': {
                    7: {'safety_rating': 'good'},
                    8: {'safety_rating': 'fair'}
                }
            }
        }
        result = process_vehicle_ids(vehicle_ids)
        self.assertEqual(result, expected_result)

    # Testing for varying length vehicle ids per year
    @patch('SafetyRatingsWVehicleIds.get_safety_ratings_for_vehicle')
    def test_process_vehicle_ids_w_diff_length(self, mock_get_safety_ratings_for_vehicle):
        vehicle_ids = {
            'Acura': {
                '2020': [1, 2, 3],
                '2021': [4, 5]
            },
            'Honda': {
                '2020': [6, 7],
                '2021': [8]
            }
        }
        mock_get_safety_ratings_for_vehicle.side_effect = [
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 1
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 2
            {'safety_rating': 'fair'},  # Safety rating for vehicle ID 3
            {'safety_rating': 'poor'},  # Safety rating for vehicle ID 4
            {'safety_rating': 'average'},  # Safety rating for vehicle ID 5
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 6
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 7
            {'safety_rating': 'fair'}  # Safety rating for vehicle ID 8
        ]
        expected_result = {
            'Acura': {
                '2020': {
                    1: {'safety_rating': 'excellent'},
                    2: {'safety_rating': 'good'},
                    3: {'safety_rating': 'fair'}
                },
                '2021': {
                    4: {'safety_rating': 'poor'},
                    5: {'safety_rating': 'average'}
                }
            },
            'Honda': {
                '2020': {
                    6: {'safety_rating': 'excellent'},
                    7: {'safety_rating': 'good'}
                },
                '2021': {
                    8: {'safety_rating': 'fair'}
                }
            }
        }
        result = process_vehicle_ids(vehicle_ids)
        self.assertEqual(result, expected_result)

    # Testing for an empty list
    @patch('SafetyRatingsWVehicleIds.get_safety_ratings_for_vehicle')
    def test_process_vehicle_ids_with_empty_list(self, mock_get_safety_ratings_for_vehicle):
        # Simulate an empty list of vehicle IDs
        vehicle_ids = {}

        # Mock the get_safety_ratings_for_vehicle function
        mock_get_safety_ratings_for_vehicle.return_value = {}

        # Expected result should also be an empty dictionary
        expected_result = {}

        # Call the process_vehicle_ids function with the empty list of vehicle IDs
        result = process_vehicle_ids(vehicle_ids)

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)

    # Testing for varying large numbers as vehicle ids
    @patch('SafetyRatingsWVehicleIds.get_safety_ratings_for_vehicle')
    def test_process_vehicle_ids_w_large_nums(self, mock_get_safety_ratings_for_vehicle):
        vehicle_ids = {
            'Acura': {
                '2020': [11111, 22222, 33333],
                '2021': [44444, 55555]
            },
            'Honda': {
                '2020': [66666, 77777],
                '2021': [88888]
            }
        }
        mock_get_safety_ratings_for_vehicle.side_effect = [
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 1
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 2
            {'safety_rating': 'fair'},  # Safety rating for vehicle ID 3
            {'safety_rating': 'poor'},  # Safety rating for vehicle ID 4
            {'safety_rating': 'average'},  # Safety rating for vehicle ID 5
            {'safety_rating': 'excellent'},  # Safety rating for vehicle ID 6
            {'safety_rating': 'good'},  # Safety rating for vehicle ID 7
            {'safety_rating': 'fair'}  # Safety rating for vehicle ID 8
        ]
        expected_result = {
            'Acura': {
                '2020': {
                    11111: {'safety_rating': 'excellent'},
                    22222: {'safety_rating': 'good'},
                    33333: {'safety_rating': 'fair'}
                },
                '2021': {
                    44444: {'safety_rating': 'poor'},
                    55555: {'safety_rating': 'average'}
                }
            },
            'Honda': {
                '2020': {
                    66666: {'safety_rating': 'excellent'},
                    77777: {'safety_rating': 'good'}
                },
                '2021': {
                    88888: {'safety_rating': 'fair'}
                }
            }
        }
        result = process_vehicle_ids(vehicle_ids)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
