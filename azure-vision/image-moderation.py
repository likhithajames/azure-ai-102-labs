from dotenv import load_dotenv
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def AnalyzeImage():
    features = [VisualFeatureTypes.adult]

    with open("image.jpg", "rb") as image_stream:
        analysis = computervision_client.analyze_image_in_stream(image_stream, visual_features=features)    

    # Get moderation ratings
    ratings = 'Ratings:\n -Adult: {}\n -Racy: {}\n -Gore: {}'.format(analysis.adult.is_adult_content,
                                                                        analysis.adult.is_racy_content,
                                                                        analysis.adult.is_gory_content)
    print(ratings)

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