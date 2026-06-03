from dotenv import load_dotenv
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

try:
    load_dotenv()
    
    inputString = input("Enter the string to be extracted:")
   
    endpoint = os.getenv("ENDPOINT")
    key = os.getenv("KEY")

    credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint, credential)

    result = client.extract_key_phrases([inputString])
    key_phrases = result[0]

    if key_phrases.is_error:
        print(f"Error extracting key phrases: {key_phrases.error.code} - {key_phrases.error.message}")
    else:
        print(f"Key Phrases: {','.join(key_phrases.key_phrases)}")

except Exception as err:
    print(f"Encountered exception. {err}")
