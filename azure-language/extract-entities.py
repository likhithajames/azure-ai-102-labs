from dotenv import load_dotenv
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

try:
    load_dotenv()
    typeOfInput = input("Enter 1 for input string and 2 for input file from sample.txt: ")
    if(typeOfInput == '1'):
         inputString = input("Enter the string to be extracted:")
    else:
        with open('sample.txt', 'r',encoding='utf8' ) as file:
            inputString = file.read()

    endpoint = os.getenv("ENDPOINT")
    key = os.getenv("KEY")

    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint, credential)

    result = client.recognize_entities([inputString])
    entities = result[0]

    if entities.is_error:
        print(f"Error recognizing entities: {entities.error.code} - {entities.error.message}")
    else:
        for entity in entities.entities:
            print(f"Name: {entity.text} Category: {entity.category} Confidence Score: {entity.confidence_score}")

except Exception as err:
    print(f"Encountered exception. {err}")
