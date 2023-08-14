# -*- coding: utf-8 -*-
import requests
import pymysql
import json
from flask import Flask, render_template, request, jsonify
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
import time
from flasgger import Swagger


from slack_bolt.adapter.socket_mode import SocketModeHandler
import certifi
import ssl

from request import request_bp
from database import connect_db, get_api_info_by_id, insert_api_info, delete_api_by_id,update_api_by_id

from config import (
    # DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,API_URL, HEADERS, DATA, 
    SLACK_BOT_TOKEN, SLACK_USER_ID
)

app = Flask(__name__)

Swagger(app)


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
    #Swagger annotation
    """Get All API Info
    ---
    responses:
        200:
            description: List of API Info
            schema:
                id: API Info
                properties:
                    ID:
                        type: integer
                        description: The API ID
                        default: 1
                    API_NM:
                        type: string
                        description: The API Name
                        default: API Name
                    API_URL:
                        type: string
                        description: The API URL
                        default: API URL
                    API_HEADER:
                        type: string
                        description: The API Header
                        default: API Header
                    API_BODY:
                        type: string
                        description: The API Body
                        default: API Body
                    API_DESC:
                        type: string
                        description: The API Description
                        default: API Description
    """


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


@app.route('/send_slack_dm', methods=['POST'])
def send_slack_dm():

    data = request.get_json()
    # api_url = data.get('api_url')
    message = data.get('message')

    ssl._create_default_https_context = ssl._create_unverified_context

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    if not message:
        return {'error': 'Please provide the message to send'}, 400

    try:
        client = WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context) 
        # client = WebClient(token=SLACK_BOT_TOKEN)
        
        response = client.chat_postMessage(channel=SLACK_USER_ID, text=message)
        return {'message': 'API Request sent successfully'}
    except SlackApiError as e:
        return {'error': f'Slack API error: {e.response["error"]}'}, 500


@app.route('/request')
def request_page():
    return render_template('request.html')

app.register_blueprint(request_bp, url_prefix='/request')

# schedule.every().day.at("09:50").do(scheduled_api_request)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # run_schedule()
    app.run(debug=True)
