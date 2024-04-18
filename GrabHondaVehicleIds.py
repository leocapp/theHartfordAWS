import json
import urllib.request


def get_vehicle_ids_for_model_year(make, model, year):
    # Make a request to NHTSA API to get vehicle IDs for a specific make, model, and year
    url = f'https://api.nhtsa.gov/SafetyRatings/modelyear/{year}/make/{make}/model/{model}?format=json'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    # Extract vehicle IDs from the API response
    vehicle_ids = [result['VehicleId'] for result in data.get('Results', [])]
    return vehicle_ids


def aggregate_vehicle_ids(models, start_year, end_year):
    all_vehicle_ids = {}
    for model in models:
        make = model['Make_Name']
        model_name = model['Model_Name']
        if ' ' in model_name:
            model_name = model_name.replace(' ', '%20')
        model_ids = model['Model_ID']
        model_vehicle_ids = {}
        for year in range(start_year, end_year + 1):
            vehicle_ids = get_vehicle_ids_for_model_year(make, model_name, year)
            model_vehicle_ids[str(year)] = vehicle_ids
        all_vehicle_ids[model_name] = model_vehicle_ids
    return all_vehicle_ids


def lambda_handler(event, context):
    # Specify the S3 bucket name and file key containing the models data
    # s3_bucket_name = 'web-wizards'
    # s3_file_key = 'car_models_test.json'  # file name
    # Get Acura models from the S3 file
    # acura_models = get_models_from_s3(s3_bucket_name, s3_file_key)

    # Specify the start and end years
    start_year = 2020
    end_year = 2023

    # Aggregate vehicle IDs for Acura models
    # all_vehicle_ids = aggregate_vehicle_ids(acura_models, start_year, end_year)

    # Upload aggregated data to S3
    # upload_to_s3(all_vehicle_ids)
