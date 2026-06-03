from dotenv import load_dotenv
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def AnalyzeImage():
    features = [VisualFeatureTypes.categories]

    with open("building.jpg", "rb") as image_stream:
        analysis = computervision_client.analyze_image_in_stream(image_stream, visual_features=features)    

    # Get image categories
    if (len(analysis.categories) > 0):
        print("Categories:")
        landmarks = []
        for category in analysis.categories:
            # Print the category
            print(" -'{}' (confidence: {:.2f}%)".format(category.name, category.score * 100))
            if category.detail:
                # Get landmarks in this category
                if category.detail.landmarks:
                    for landmark in category.detail.landmarks:
                        if landmark not in landmarks:
                            landmarks.append(landmark)

        # If there were landmarks, list them
        if len(landmarks) > 0:
            print("Landmarks:")
            for landmark in landmarks:
                print(" -'{}' (confidence: {:.2f}%)".format(landmark.name, landmark.confidence * 100))
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