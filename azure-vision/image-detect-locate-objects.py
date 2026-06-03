from dotenv import load_dotenv
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw

def AnalyzeImage():
    features = [VisualFeatureTypes.objects]

    with open("building.jpg", "rb") as image_stream:
        analysis = computervision_client.analyze_image_in_stream(image_stream, visual_features=features)    

        # Prepare image for drawing
        fig = plt.figure(figsize=(8, 8))
        plt.axis('off')
        image = Image.open("building.jpg")
        draw = ImageDraw.Draw(image)
        color = 'cyan'
        for detected_object in analysis.objects:
            # Print object name
            print(" -{} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))
            
            # Draw object bounding box
            r = detected_object.rectangle
            bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
            draw.rectangle(bounding_box, outline=color, width=3)
            plt.annotate(detected_object.object_property,(r.x, r.y), backgroundcolor=color)
        # Save annotated image
        plt.imshow(image)
        outputfile = 'objects.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)

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