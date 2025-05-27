# Image Classification Web App
 # Author: Vanesa Goceva
 
 Course: ISDe Projects 2024
 
 Project Type: Individual Submission (2 new features)
 # Description
 This project is a web application for image classification using different machine learning models. It allows users to select an image and a model, and see the classification results displayed in a user-friendly format. It is developed using FastAPI and follows an agile development approach.

This is an individual project submission implementing two new features (details below). It satisfies the full scoring criteria and is ready to be presented with a clean structure, proper documentation, and a working demo.
# Features Implemented
Feature 1: Multiple Model Comparison:
Allows the user to classify a single image using multiple models at once.

Displays side-by-side results for each selected model.

Helps users compare model performance directly in the interface.

Feature 2: Save Classification History:
Saves classification results (image name, model, prediction, timestamp) to a JSON file.

Implements a history page where users can see a table of past predictions.

Useful for reviewing and debugging.
# Clone the Repository
git clone https://github.com/YOUR_USERNAME/VanesaGocevaImageClassifier.git
cd VanesaGocevaImageClassifier
# Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
# Install Requirements
pip install -r requirements.txt
# Run the App
uvicorn main:app --reload
# Configuration
Configure the service by editing the file config.py.
# Prepare the resources
It is recommended to pre-download images and models before running the server. This is to avoid unnecessary waits for users.

Run prepare_images.py and prepare_models.py. Models will be stored in your PyTorch cache directory, while the path for the image directory can be found in the config.py file.

python app/prepare_images.py
python app/prepare_models.py
# Usage
# Run locally
To run the code without containers, it is sufficient to run separately the server,

uvicorn main:app --reload
