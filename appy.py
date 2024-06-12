import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify,render_template
from sqlalchemy import create_engine
import sqlite3
import joblib
import cohere
import cv2
import matplotlib.pyplot as plt
from prodiapy import Prodia
import requests
from io import BytesIO

app = Flask(__name__)

co = cohere.Client(api_key="lOGO9JDezVva0OyZAzvPOQUjlq8fUw0nJ0WeL0fS")
prompt = """necesito generar frases de felicitación de navidad para mi familia con un máximo de 5 palabras.
tu respuesta debe ser directamente la felicitación navideña con las 8 palabras como máximo, por favor, no
devuelvas mas palabras que eso"""
response = co.generate(
                    model = "command-nightly",
                    prompt = prompt,
                    max_tokens = 15,
                    temperature = 0.01,
                    k=0,
                    p = 0.75,
                    stop_sequences = [],
                    return_likelihoods = "NONE"
                    )

nav = response.generations[0].text
nav

prodia = Prodia(
    api_key="036b6793-faa1-477c-b3c3-2b3af9b1afed"
)

job = prodia.sd.generate(prompt="Birthday cake")
result = prodia.wait(job)

result.image_url

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/retorno', methods=['POST'])

def retorno():
        

        return render_template("retorno.html",prediction=)
        # return 

if __name__ == '__main__':
    app.run(debug=True)