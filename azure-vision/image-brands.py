from dotenv import load_dotenv
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def AnalyzeImage():
    features = [VisualFeatureTypes.brands]
    with open("person.jpg", "rb") as image_stream:
        analysis = computervision_client.analyze_image_in_stream(image_stream, visual_features=features)    
        print("brands count:", len(analysis.brands))
        print("raw brands:", analysis.brands)
        
    #Print the brands in the image
    for brand in analysis.brands:
        print(f"brands: {brand.name}\nConfidence: {brand.confidence:.2f}")

try:
    load_dotenv()
    
    endpoint = os.getenv("ENDPOINT")
    key = os.getenv("KEY")
   
    #Load image
    image = "image.jpg"

    #configuration - computer vision
    credentials = CognitiveServicesCredentials(key)
    computervision_client = ComputerVisionClient(endpoint, credentials)

    #analyze the image
    AnalyzeImage()

except Exception as err:
    print(f"Encountered exception. {err}")