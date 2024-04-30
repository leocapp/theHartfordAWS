import json
import pymysql
import boto3
import json


rds_host = 'nhtsa-db.cze20essmpxj.us-east-1.rds.amazonaws.com'
rds_user = 'admin'
rds_password = 'WebWizards101'
rds_db_name = 'nhtsa_info'
conn = pymysql.connect(host=rds_host, user=rds_user, password=rds_password, db=rds_db_name, connect_timeout=20)
safetydict = {0: "id", 1: "Year", 2: "Vehicle_ID", 3: "OverallRating", 4: "Make", 5: "Model", 6: "VehicleDescription", 7: "ComplaintsCount", 8: "VehiclePicture",9: "FrontCrashPicture", 10: "SideCrashPicture", 11: "SidePolePicture", 12: "FrontCrashVideo", 13: "SideCrashVideo", 14: "SidePoleVideo", 15: "OverallFrontCrashRating", 16: "OverallSideCrashRating", 17: "RolloverRating", 18: "RecallsCount", 19: "InvestigationCount"}



def database_to_api_gateway(req_body, context):
    with conn.cursor() as cur:
        sqlBuilder = "SELECT * from SafetyRatings where "
        if req_body["Year"] !=  "": 
            sqlBuilder += "Year={}".format(req_body["Year"])
            if req_body["Make"] != "" or req_body["Model"] != "":
                sqlBuilder += " AND "

        if req_body["Make"] != "":
            sqlBuilder += "Make=\"{}\"".format(req_body["Make"])
            if req_body["Model"] != "":
                sqlBuilder += " AND "

        if req_body["Model"] != "":
            sqlBuilder += "Model=\"{}\"".format(req_body["Model"])

        print(sqlBuilder)
        cur.execute(sqlBuilder)
        print("Query executed")
        safety_details = []
        try:
            for rating in cur.fetchall():
                safety_detail = {}
                for row in range(0, len(rating)):
                    safety_detail[safetydict[row]] = rating[row]
                safety_details.append(safety_detail)
        except Exception as e:
            print(e)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(safety_details)
    }