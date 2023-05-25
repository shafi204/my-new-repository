from email import header
import requests
from pymongo import MongoClient

API_URL = "https://rbos.service-now/myserviceportal?id=managed_incidents"
MongoDB_connection_string = "mongodb://localhost:27017"
Database_name = "Managed_incidents"
Collection_name = "Incidents"

def log_incident(api_key, title, description):
    headers = {"Authorisation": f"Bearer {api_key}"}
    data = {
        "Title": title,
        "Description": description
    } 
    response = requests.post(API_URL, headers=headers , json=data)

    if response.status_code == 201:
        print("Incident logged successfully.")
    else:
        print("Failed to log incident.")
        print("Error:", response.text)

def save_incident_to_mongoDB(title, description):
    client = MongoClient(MongoDB_connection_string)
    db = client[Database_name]   
    collection = db[Collection_name]    

    incident = {
        "title": title,
        "description": description
    }

    result = collection.insert_one(incident)
    client.close()

    if result.inserted_id:
        print("Incident saved to MongoDB.")
    else:
        print("Failed to save incident to MongoDB.")

def main():
    api_key = input("Enter your API key: ")

    title = input("Enter incident title: ")
    description = input("Enter incident description: ")

    log_incident(api_key, title, description)



    