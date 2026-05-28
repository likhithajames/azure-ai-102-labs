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

    result = client.detect_language([inputString])
    language = result[0]

    if language.is_error:
        print(f"Error detecting language: {language.error.code} - {language.error.message}")
    else:
        print(f"Language: {language.primary_language.name} Confidence Score: {language.primary_language.confidence_score}")

except Exception as err:
    print(f"Encountered exception. {err}")
