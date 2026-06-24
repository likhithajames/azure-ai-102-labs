import os
import sys
from dotenv import load_dotenv

from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import ContainerClient

load_dotenv()

endpoint = os.getenv("FORM_ENDPOINT")
key = os.getenv("FORM_KEY")
training_data_url = os.getenv("STORAGE_URL")

if not endpoint or not key or not training_data_url:
    print("Missing env vars. Ensure FORM_ENDPOINT, FORM_KEY and STORAGE_URL are set in .env")
    sys.exit(1)

# Quick check: can we list blobs in the container (SAS must include List permission 'l')?
try:
    container_client = ContainerClient.from_container_url(training_data_url)
    # attempt to fetch one blob to verify permissions
    blobs = container_client.list_blobs()
    next(blobs, None)
except Exception as e:
    print(f"Cannot access STORAGE_URL container: {e}")
    print("Ensure the STORAGE_URL is a container SAS URL (https://<acct>.blob.core.windows.net/<container>?<SAS>) with at least Read and List permissions.")
    sys.exit(1)

# create clients
form_recognizer_client = FormRecognizerClient(endpoint=endpoint, credential=AzureKeyCredential(key))
form_training_client = FormTrainingClient(endpoint=endpoint, credential=AzureKeyCredential(key))

try:
    poller = form_training_client.begin_training(training_data_url, use_training_labels=True)
    model = poller.result()
    print(f"Model ID: {model.model_id}")
    print(f"Model Status: {model.status}")
    print(f"Model Training Started On: {model.training_started_on}")
    print(f"Model Training Completed On: {model.training_completed_on}")
    if model.status.lower() != "ready":
        print("Model created but not ready. Check training data permissions/format and training labels.")
except Exception as e:
    print(f"An error occurred during training: {e}")
    sys.exit(1)