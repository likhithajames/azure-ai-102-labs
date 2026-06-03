from dotenv import load_dotenv
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def AnalyzeImage():
    print('Generating thumbnail')

    # Generate a thumbnail
    with open("image.jpg", mode="rb") as image_data:
        # Get thumbnail data
        thumbnail_stream = computervision_client.generate_thumbnail_in_stream(100, 100, image_data, True)

    # Save thumbnail image
    thumbnail_file_name = 'thumbnail.png'
    with open(thumbnail_file_name, "wb") as thumbnail_file:
        for chunk in thumbnail_stream:
            thumbnail_file.write(chunk)

    print('Thumbnail saved in.', thumbnail_file_name)

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