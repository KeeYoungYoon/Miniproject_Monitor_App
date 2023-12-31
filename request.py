# request.py
from flask import Blueprint,request, jsonify
import requests

import time
import ssl
import certifi
import json
from config import API_URL, HEADERS, DATA, SLACK_BOT_TOKEN, SLACK_USER_ID
from database import update_api_request_rslt_by_id

request_bp = Blueprint('request_bp', __name__)
@request_bp.route('/make_api_request', methods=['POST'])
def make_api_request():
    data = request.get_json()
    apiId = data.get('apiId')
    apiUrl = data.get('apiUrl')
    apiHeader = data.get('apiHeader')
    apiBody = data.get('apiBody')

    if apiUrl and apiHeader and apiBody:
        # print('here here')
        print(apiUrl)
        print(apiHeader)
        print(apiBody)

        try:
            apiHeader_dict = json.loads(apiHeader)

            response = requests.post(apiUrl, headers=apiHeader_dict, json=apiBody, verify=False)
            # response = requests.get(apiUrl, headers=apiHeader_dict, verify=False)
            print(response.status_code)
            print(response.content)

            if response.status_code == 200:
                update_api_request_rslt_by_id(apiId, "Y")
                # send_slack_dm()
                return response.json()
            else:
                update_api_request_rslt_by_id(apiId, "N")
                # If there was an error, return the error message
                return {'error': f'API request failed with status code: {response.status_code}'}, response.status_code
        except Exception as e:
            print(response.status_code)
            print(response.content)
            print('Exception:', str(e))  # Print the exception for debugging purposes
            update_api_request_rslt_by_id(apiId, "N")
            return {'error': 'An internal server error occurred.'}, 500
    else:
        update_api_request_rslt_by_id(apiId, "N")
        return {'message': 'Please provide all required API data'}, 400
    
