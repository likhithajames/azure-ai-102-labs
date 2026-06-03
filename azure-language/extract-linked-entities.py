from dotenv import load_dotenv
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

try:
    load_dotenv()
    
    inputString = input("Enter the string to be converted:")
   
    endpoint = os.getenv("ENDPOINT")
    key = os.getenv("KEY")

    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint, credential)

    result = client.recognize_linked_entities([inputString])
  
    linked_entities = result[0]

    if linked_entities.is_error:
        print(f"Error recognizing linked entities: {linked_entities.error.code} - {linked_entities.error.message}")
    else:
        for entity in linked_entities.entities:
            print(f"Name: {entity.name} URL: {entity.url} Data Source: {entity.data_source}")
        
except Exception as err:
    print(f"Encountered exception. {err}")
