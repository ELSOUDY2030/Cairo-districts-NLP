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
    git clone https://github.com/yourusername/cairo-classifier.git
    cd cairo-classifier
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Training the LSTM model:

    ```bash
    # Add instructions to train the LSTM model
    ```

4. Running the FastAPI:

    ```bash
    # Add instructions to run the FastAPI server
    ```

## Usage

Explain how users can use your project, make predictions using the API, and any other relevant information.

## Docker

To run the project using Docker, follow these steps:

```bash
# docker container run -it -v C:\clone\location:/docker -p 8501:8501 --name nlp deep/NLP:v1.0

