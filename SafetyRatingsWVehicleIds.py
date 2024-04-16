import json
import urllib.request
import boto3
import time

s3 = boto3.client('s3')


def get_safety_ratings_for_vehicle(vehicle_id):
    url = f'https://api.nhtsa.gov/SafetyRatings/VehicleId/{vehicle_id}?format=json'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data


def process_vehicle_ids(vehicle_ids):
    safety_ratings = {}
    for model, year_data in vehicle_ids.items():
        safety_ratings[model] = {}
        for year, ids in year_data.items():
            safety_ratings[model][year] = {}
            for vehicle_id in ids:
                safety_data = get_safety_ratings_for_vehicle(vehicle_id)
                safety_ratings[model][year][vehicle_id] = safety_data
                time.sleep(0.1)  # Introduce a 0.1-second delay
    return safety_ratings


def lambda_handler(event, context):
    # Specify the bucket name and file key where the vehicle IDs file is stored
    bucket_name = 'web-wizards'
    file_key = 'all_vehicle_ids.json'

    # Retrieve the file content from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')

    # Parse the JSON data from the file
    vehicle_ids = json.loads(file_content)

    # Process vehicle IDs to get safety ratings
    safety_ratings = process_vehicle_ids(vehicle_ids)

    # Upload safety ratings data to another S3 bucket
    target_bucket_name = 'safety-ratings'
    target_object_key = 'test_all_safety_ratings.json'
    s3.put_object(Body=json.dumps(safety_ratings), Bucket=target_bucket_name, Key=target_object_key)
