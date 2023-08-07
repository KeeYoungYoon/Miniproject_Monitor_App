# -*- coding: utf-8 -*-
import requests
import pymysql
import json
from flask import Flask, render_template, request, jsonify
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


from slack_bolt.adapter.socket_mode import SocketModeHandler
import certifi
import ssl




app = Flask(__name__)

# Database configuration
DB_HOST = #'MariaDB host'
DB_USER = #'MariaDB username'
DB_PASSWORD = #'MariaDB password'
DB_NAME = #'MariaDB database name'

# Function to connect to the database
def connect_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

# Function to get API_NM by id from the database
def get_api_info_by_id(ID):
    connection = connect_db()
    cursor = connection.cursor()

    query = "SELECT ID, API_NM, API_URL, API_HEADER, API_BODY, API_DESC FROM API_INFO WHERE ID = %s"
    cursor.execute(query, (ID,))
    result = cursor.fetchone()

    connection.close()

    if result:
        return {
            'ID': result[0],
            'API_NM': result[1],
            'API_URL': result[2],
            'API_HEADER': result[3],
            'API_BODY': result[4],
            'API_DESC': result[5],
        }
    else:
        return None

# Function to insert data into the database
def insert_api_info(api_name, api_url, api_header, api_body, api_desc):
    connection = connect_db()
    cursor = connection.cursor()

    query = "INSERT INTO API_INFO (API_NM, API_URL, API_HEADER, API_BODY, API_DESC) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (api_name, api_url, api_header, api_body, api_desc))
    connection.commit()

    connection.close()

# Function to delete API by ID
def delete_api_by_id(ID):
    connection = connect_db()
    cursor = connection.cursor()

    query = "DELETE FROM API_INFO WHERE ID = %s"
    cursor.execute(query, (ID,))
    connection.commit()

    connection.close()

def update_api_by_id(ID, api_name, api_url, api_header, api_body, api_desc):
    connection = connect_db()
    cursor = connection.cursor()

    query = "UPDATE API_INFO SET API_NM = %s, API_URL = %s, API_HEADER = %s, API_BODY = %s, API_DESC = %s WHERE ID = %s"
    cursor.execute(query, (api_name, api_url, api_header, api_body, api_desc, ID))
    connection.commit()

    connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_api_info')
def insert_api_info_page():
    return render_template('insert_api_info.html')

@app.route('/insert_api', methods=['POST'])
def insert_api():
    data = request.get_json()
    api_name = data.get('api_name')
    api_url = data.get('api_url')
    api_header = data.get('api_header')
    api_body = data.get('api_body')
    api_desc = data.get('api_desc')

    if api_name and api_url and api_header and api_body and api_desc:
        insert_api_info(api_name, api_url, api_header, api_body, api_desc)
        return jsonify({'message': 'API Info inserted successfully'}), 200
    else:
        return jsonify({'message': 'Please provide all required information.'}), 400

@app.route('/delete_api', methods=['POST'])
def delete_api():
    data = request.get_json()
    ID = data.get('ID')

    if ID:
        delete_api_by_id(ID)
        return jsonify({'message': f'Deleted API with ID: {ID}'}), 200
    else:
        return jsonify({'message': 'Please provide the ID to delete the API.'}), 400

@app.route('/update_api', methods=['POST'])
def update_api():
    data = request.get_json()
    ID = data.get('ID')
    api_name = data.get('api_name')
    api_url = data.get('api_url')
    api_header = data.get('api_header')
    api_body = data.get('api_body')
    api_desc = data.get('api_desc')

    if not ID or not api_name or not api_url or not api_header or not api_body or not api_desc:
        return jsonify({'message': 'Please enter all required information.'}), 400

    update_api_by_id(ID, api_name, api_url, api_header, api_body, api_desc)
    return jsonify({'message': f'Updated API with ID: {ID}'}), 200

# Route to get all API information
@app.route('/get_all_api_info')
def get_all_api_info():
    connection = connect_db()
    cursor = connection.cursor()

    query = "SELECT ID, API_NM, API_URL, API_HEADER, API_BODY, API_DESC FROM API_INFO"
    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()

    api_info_list = []
    for row in result:
        api_info_list.append({
            'ID': row[0],
            'API_NM': row[1],
            'API_URL': row[2],
            'API_HEADER': row[3],
            'API_BODY': row[4],
            'API_DESC': row[5],
        })

    return jsonify(api_info_list), 200

@app.route('/make_api_request', methods=['POST'])
def make_api_request():
    data = request.get_json()
    apiUrl = data.get('apiUrl')
    apiHeader = data.get('apiHeader')
    apiBody = data.get('apiBody')

    if apiUrl and apiHeader and apiBody:
        print(apiUrl)
        print(apiHeader)
        print(apiBody)

        try:

            apiHeader_dict = json.loads(apiHeader)

            API_URL = #'url'
            HEADERS =#'headers'
            data = 'data'

            # response = requests.post(API_URL, headers=HEADERS, json=data, verify=False)

            response = requests.post(API_URL, headers=HEADERS, json=data, verify=False)
            
            print(response.status_code)
            print(response.content)

            # response = requests.post(apiUrl, headers=apiHeader_dict, json=apiBody, verify=False)

            # Check the status code of the response
            if response.status_code == 200:
                return response.json()
            else:
                # If there was an error, return the error message
                return {'error': f'API request failed with status code: {response.status_code}'}, response.status_code
        except Exception as e:
            print(response.status_code)
            print(response.content)
            print('Exception:', str(e))  # Print the exception for debugging purposes
            return {'error': 'An internal server error occurred.'}, 500
    else:
        return {'message': 'Please provide all required API data'}, 400



SLACK_BOT_TOKEN = #'token'
SLACK_USER_ID = #'user_id'

@app.route('/send_slack_dm', methods=['POST'])
def send_slack_dm():
    data = request.get_json()
    message = data.get('message')

    ssl._create_default_https_context = ssl._create_unverified_context

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    if not message:
        return {'error': 'Please provide the message to send'}, 400

    try:
        client = WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context) 
        # client = WebClient(token=SLACK_BOT_TOKEN)
        
        response = client.chat_postMessage(channel=SLACK_USER_ID, text=message)
        return {'message': 'Slack DM sent successfully'}
    except SlackApiError as e:
        return {'error': f'Slack API error: {e.response["error"]}'}, 500


@app.route('/make_test_api_request', methods=['POST'])
def make_test_api_request():
    data = request.get_json()
    apiUrl = data.get('apiUrl')
    apiHeader = data.get('apiHeader')
    apiBody = data.get('apiBody')

    if apiUrl and apiHeader and apiBody:
        try:
            apiHeader_dict = json.loads(apiHeader)
            response = requests.post(apiUrl, headers=apiHeader_dict, json=apiBody, verify=False)

            if response.status_code == 200:
                # send_slack_dm()
                return response.json()
            else:
                return {'error': f'API request failed with status code: {response.status_code}'}, response.status_code
        except Exception as e:
            return {'error': str(e)}, 500
    else:
        return {'message': 'Please provide all required API data'}, 400

@app.route('/request')
def request_page():
    return render_template('request.html')

if __name__ == '__main__':
    app.run(debug=True)
