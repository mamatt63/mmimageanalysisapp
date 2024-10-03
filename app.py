import streamlit as st

# importing os module for environment variables and dotenv functions
import os
from dotenv import load_dotenv 

# import azure libraries
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# loading variables from .env file
load_dotenv() 

# accessing vision key and endpoint
subscription_key = os.getenv("VISION_KEY")
endpoint = os.getenv("VISION_ENDPOINT")

# Authenticates your credentials and creates a client.
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Define the image to analyse
remote_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Chichen_Itza_3.jpg/1920px-Chichen_Itza_3.jpg"

# Call AI Vision API to analyse a remote image
tags_result_remote = computervision_client.tag_image(remote_image_url)

# Show results with confidence score
st.markdown("Tags in the remote image: ")
if (len(tags_result_remote.tags) == 0):
    st.text("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        st.text("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

# this is the main function in which we define our webpage  
def main():
    st.markdown("# Image Analysis App 🖼️")
    st.markdown("### This app allows you to extract visual features from images.")

# Init code
if __name__=='__main__': 
    main()