# Cairo-districts-NLP

## Overview

Cairo-Classifier is a project that classifies headlines based on whether they are related to Cairo or not. It utilizes LSTM model, TensorFlow, Docker, and the API from here.com. Additionally, a FastAPI is implemented to create an API for serving predictions.

## Project Structure

- **`src/`**: Contains the source code for the project.
  - **`models/`**: Stores the LSTM model implementation.
  - **`api/`**: Implements the FastAPI for serving predictions.
- **`data/`**: Holds any necessary data files for training or testing.
- **`docker/`**: Includes Docker-related files.
- **`requirements.txt`**: Lists all the required dependencies for the project.

## Setup

1. Clone the repository:

    ```bash
    https://github.com/ELSOUDY2030/Cairo-districts-NLP.git
    cd cairo-classifier
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Running the FastAPI:

    ```bash
    # uvicorn main:app
    ```

## Docker

To run the project using Docker, follow these steps:

```bash
# docker container run -it -v C:\clone\location:/docker -p 8501:8501 --name nlp deep/NLP:v1.0





