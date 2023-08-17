import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

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

# Function to update REQUEST_RSLT, REQUEST_DTM by ID, REQUEST_DTM should be current time
def update_api_request_rslt_by_id(ID, request_rslt):
    print("updating db", ID, request_rslt)
    connection = connect_db()
    cursor = connection.cursor()
    if(request_rslt == "Y"):
         query = "UPDATE API_INFO SET REQUEST_RSLT = %s, REQUEST_DTM = now(), LAST_SUCS_REQ_DTM = now() WHERE ID = %s"
    else:
         query = "UPDATE API_INFO SET REQUEST_RSLT = %s, REQUEST_DTM = now() WHERE ID = %s"
    
    
    cursor.execute(query, (request_rslt, ID))
    connection.commit()

    connection.close()

#Function to get all API information
def get_all_api_info():
    connection = connect_db()
    cursor = connection.cursor()

    query = "SELECT ID, API_NM, API_URL, API_HEADER, API_BODY, API_DESC, REQUEST_RSLT,REQUEST_DTM,LAST_SUCS_REQ_DTM FROM API_INFO"
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
            'REQUEST_RSLT': row[6],
            'REQUEST_DTM': row[7],
            'LAST_SUCS_REQ_DTM': row[8]
        })

    return api_info_list

