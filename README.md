# AgroShield

## Smart Crop Health Assessment Web Application

AgroShield is a web-based crop health assessment application designed to help farmers and agricultural users identify possible crop problems from a crop image and current field weather conditions.

The application combines a user-provided crop image, crop name, geographical location, and current weather information to generate a preliminary crop health assessment and practical field guidance.

## Problem Statement

Farmers may notice symptoms such as leaf spots, yellowing, curling, holes, discoloration, and drying but may not immediately know what could be causing them.

At the same time, environmental conditions such as humidity, rainfall, temperature, and wind can influence crop disease development and the effectiveness of field treatments.

AgroShield provides these factors together in a simple web interface so that users can receive an initial assessment and decide whether further inspection or expert consultation is required.

## Features

* Crop name input
* Crop image upload
* Location detection using the browser's geolocation feature
* Current weather information based on the user's location
* Weather-related crop risk assessment
* Preliminary crop problem identification
* Possible causes of crop stress or disease
* Recommended immediate actions
* Suggested timing for field action
* Crop-saving plan
* Prevention recommendations
* Two-stage result presentation for easier understanding
* Beginner-friendly web interface

## How It Works

The application follows this workflow:

1. The user enters the crop name.
2. The user uploads an image of the affected crop or leaf.
3. The user selects "Use My Location".
4. The browser obtains the user's latitude and longitude.
5. The application retrieves current weather information for that location.
6. The crop name and weather conditions are evaluated by the assessment logic.
7. AgroShield presents weather conditions, visual inspection guidance, possible problems, and possible causes.
8. The user can continue to the action plan.
9. The application provides recommended actions, timing, crop-saving steps, and prevention guidance.

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Weather Data

* Open-Meteo API

### Location

* Browser Geolocation API

### Assessment Logic

The current version uses rule-based assessment logic based on:

* Crop name
* Relative humidity
* Rainfall
* Wind speed
* Temperature
* General crop-health knowledge

The uploaded image is received by the application and used as part of the assessment workflow, but the current version does not contain a trained computer-vision model that independently diagnoses diseases from image pixels.

## Project Structure

```text
AgroShield/
│
├── app.py
├── weather.py
├── advisory.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Main Files

### app.py

Runs the Flask web application, handles the web interface, receives the crop information, image, and location, and returns the assessment results.

### weather.py

Retrieves current weather conditions using the Open-Meteo service.

### advisory.py

Contains the crop-health assessment rules and generates:

* Possible problem
* Weather risks
* Possible causes
* Immediate actions
* Timing recommendations
* Crop-saving plan
* Prevention advice

### index.html

Provides the user interface for entering crop information, uploading an image, obtaining location, and displaying assessment results.

### style.css

Controls the visual appearance and layout of the application.

## Installation

Python 3 is required.

Install the required packages:

```bash
pip install flask requests
```

No Hugging Face account, AI model download, or machine-learning installation is required for the current version.

## Running the Application

Open a terminal in the project directory:

```bash
python app.py
```

The Flask development server will start locally.

Open the address shown by Flask in a web browser, normally:

```text
http://127.0.0.1:5000
```

## Using the Application

1. Enter the crop name.
2. Select an affected crop or leaf image.
3. Click "Use My Location".
4. Allow location access in the browser.
5. Click "Detect & Assess".
6. Review the weather, observations, possible problem, and possible causes.
7. Click "Continue to Action Plan".
8. Review the recommended actions and crop-saving plan.

## Important Limitation

AgroShield's current assessment is preliminary and should not be treated as a confirmed plant-disease diagnosis.

The current implementation does not use a trained image-classification or computer-vision model. Therefore, it cannot reliably identify a specific disease solely from the uploaded image.

The image upload is currently part of the assessment workflow, while the main crop-health reasoning is based on the crop entered by the user and environmental conditions.

For serious or rapidly spreading crop problems, users should consult a qualified agricultural expert or local agricultural extension service.

## Future Improvements

The project can be extended with a trained computer-vision model to analyze the actual uploaded crop image.

Potential future improvements include:

* Image-based disease classification
* More crop-specific disease knowledge
* Disease probability scores
* Identification of visible symptoms from images
* Multiple image analysis
* Historical weather analysis
* Pest identification
* Regional crop recommendations
* Agricultural expert verification
* Multilingual support
* Treatment recommendations based on verified disease identification

## Project Goal

The goal of AgroShield is to provide a simple and accessible first-level crop health assessment tool that combines crop information and environmental conditions in one application.

The project is designed as a foundation that can later be extended with machine-learning-based image analysis and more advanced agricultural intelligence.

```
```
