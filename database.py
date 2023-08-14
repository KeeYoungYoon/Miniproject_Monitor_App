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

