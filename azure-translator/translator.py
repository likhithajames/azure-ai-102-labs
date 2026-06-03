from dotenv import load_dotenv
import os

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError


try:
    load_dotenv()
       
    endpoint = os.getenv("ENDPOINT")
    region = os.getenv("REGION")
    key = os.getenv("KEY")

    credential = TranslatorCredential(key,region)
    client = TextTranslationClient(endpoint=endpoint, credential=credential)
    
    target_language = ["ml","hi"]
    input_text_elements = [ InputTextItem(text = "How are you?") ]
    result = client.translate(content = input_text_elements, to=target_language)
    translation = result[0]
   
    if translation:
        for translated_text in translation.translations:
            print(f"Translated Text: {translated_text.text} Language: {translated_text.to}")

except Exception as err:
    print(f"Encountered exception. {err}")