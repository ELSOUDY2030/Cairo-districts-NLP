from fastapi import FastAPI, File, UploadFile
import numpy as np
from tensorflow import keras
import pickle

model = keras.models.load_model('model_lstm.h5')
app = FastAPI()

@app.post("/check_text/")
async def check_text(text: str):


    with open('tokenizer.pickle', 'rb') as handle:
        loaded_tokenizer = pickle.load(handle)
    
    sequences = loaded_tokenizer.texts_to_sequences([text])

    # Padding sequences to ensure uniform length
    maxlen = 20  # Define your desired sequence length
    padded_sequences = pad_sequences(sequences, maxlen=maxlen)
    re = model.predict(padded_sequences)
    if int(round(re[0][0])) == 1:
        place = "cairo"

    else:
        place = "not cairo"






    return {"text": text, "districts is": place}
