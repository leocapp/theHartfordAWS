import unittest
from unittest.mock import patch, MagicMock
from DatabaseToAPIGateway import database_to_api_gateway


class TestDatabaseToAPIGateway(unittest.TestCase):
    @patch('DatabaseToAPIGateway.database_to_api_gateway')
    def test_get_models_for_make(self, mock_get_database):
        # Mock response data
        mock_get_database.side_effect = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Credentials": "true",
                "Content-Type": "application/json"
            },
            "body": "[{\"id\": 876, \"Year\": 2020, \"Vehicle_ID\": \"14143\", \"OverallRating\": \"5\", \"Make\": "
                    "\"ACURA\", \"Model\": \"RDX\", \"VehicleDescription\": \"2020 Acura RDX SUV AWD\", "
                    "\"ComplaintsCount\": \"162\", \"VehiclePicture\": "
                    "\"https://static.nhtsa.gov/images/vehicles/13000_st0640_046.png\", \"VehicleVideo\": "
                    "\"https://static.nhtsa.gov/crashTest/videos/2020/v10556C017.wmv\", \"OverallFrontCrashRating\": "
                    "\"4\", \"OverallSideCrashRating\": \"5\", \"RolloverRating\": \"4\", \"RecallsCount\": \"4\", "
                    "\"InvestigationCount\": \"0\"}, {\"id\": 877, \"Year\": 2020, \"Vehicle_ID\": \"14142\", "
                    "\"OverallRating\": \"5\", \"Make\": \"ACURA\", \"Model\": \"RDX\", \"VehicleDescription\": "
                    "\"2020 Acura RDX SUV FWD\", \"ComplaintsCount\": \"162\", \"VehiclePicture\": "
                    "\"https://static.nhtsa.gov/images/vehicles/13000_st0640_046.png\", \"VehicleVideo\": "
                    "\"https://static.nhtsa.gov/crashTest/videos/2020/v10556C017.wmv\", \"OverallFrontCrashRating\": "
                    "\"4\", \"OverallSideCrashRating\": \"5\", \"RolloverRating\": \"4\", \"RecallsCount\": \"4\", "
                    "\"InvestigationCount\": \"0\"}]"
        }

        # Call the function
        req_body = {"Year": 2020, "Make": "", "Model": "RDX"}
        result = database_to_api_gateway(req_body, None)

        # Assert expected result
        expected_result = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Credentials": "true",
                "Content-Type": "application/json"
            },
            "body": "[{\"id\": 876, \"Year\": 2020, \"Vehicle_ID\": \"14143\", \"OverallRating\": \"5\", \"Make\": "
                    "\"ACURA\", \"Model\": \"RDX\", \"VehicleDescription\": \"2020 Acura RDX SUV AWD\", "
                    "\"ComplaintsCount\": \"162\", \"VehiclePicture\": "
                    "\"https://static.nhtsa.gov/images/vehicles/13000_st0640_046.png\", \"VehicleVideo\": "
                    "\"https://static.nhtsa.gov/crashTest/videos/2020/v10556C017.wmv\", \"OverallFrontCrashRating\": "
                    "\"4\", \"OverallSideCrashRating\": \"5\", \"RolloverRating\": \"4\", \"RecallsCount\": \"4\", "
                    "\"InvestigationCount\": \"0\"}, {\"id\": 877, \"Year\": 2020, \"Vehicle_ID\": \"14142\", "
                    "\"OverallRating\": \"5\", \"Make\": \"ACURA\", \"Model\": \"RDX\", \"VehicleDescription\": "
                    "\"2020 Acura RDX SUV FWD\", \"ComplaintsCount\": \"162\", \"VehiclePicture\": "
                    "\"https://static.nhtsa.gov/images/vehicles/13000_st0640_046.png\", \"VehicleVideo\": "
                    "\"https://static.nhtsa.gov/crashTest/videos/2020/v10556C017.wmv\", \"OverallFrontCrashRating\": "
                    "\"4\", \"OverallSideCrashRating\": \"5\", \"RolloverRating\": \"4\", \"RecallsCount\": \"4\", "
                    "\"InvestigationCount\": \"0\"}]"
        }
        self.assertEqual(result, expected_result)


if __name__ == '__main':
    unittest.main()
