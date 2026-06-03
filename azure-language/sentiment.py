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

    result = client.analyze_sentiment([inputString])
    sentiment = result[0]

    if sentiment.is_error:
        print(f"Error analyzing sentiment: {sentiment.error.code} - {sentiment.error.message}")
    else:
        print(f"Sentiment: {sentiment.sentiment} Confidence Scores: {sentiment.confidence_scores}")

except Exception as err:
    print(f"Encountered exception. {err}")
