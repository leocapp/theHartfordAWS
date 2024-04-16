import json
import urllib.request


# import boto3


def get_models_for_make(make):
    # Make a request to NHTSA API to get models for a specific make
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data.get('Results', [])


def get_all_models():
    # Get models for specified makes and combine them into a single list
    makes = ['acura', 'honda', 'chevrolet', 'toyota', 'ford']
    all_models = []
    for make in makes:
        models = get_models_for_make(make)
        # Check if models is empty before slicing
        if models:
            models = models[:15]
        # models = get_models_for_make(make)
        all_models.extend(models)
    return all_models


"""
def get_all_models():
    # Get models for specified makes and combine them into a single list
    makes = ['acura', 'honda', 'chevrolet', 'toyota', 'ford']
    all_models = []
    for make in makes:
        models = get_models_for_make(make)[:15]
        # models = get_models_for_make(make)
        all_models.extend(models)
    return all_models
"""
"""
def upload_to_s3(data):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Upload data to S3 bucket
    bucket_name = 'web-wizards'
    object_key = 'car_models_.json'
    s3.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=object_key)


def lambda_handler(event, context):
    all_models = get_all_models()
    upload_to_s3(all_models)
"""
