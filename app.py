from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from sentence_transformers import SentenceTransformer
import numpy as np

app = Flask(__name__)

# Load models
model = load_model('plagiarism_detector_model.h5')
sbert_model = SentenceTransformer('sbert_embedding_model')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    confidence = None

    if request.method == 'POST':
        source_text = request.form['source_text']
        suspect_text = request.form['suspect_text']

        # Encode texts
        embedding1 = sbert_model.encode([source_text])
        embedding2 = sbert_model.encode([suspect_text])

        # Add noise (optional, if you used during training)
        noise_factor = 0.01
        embedding1 += noise_factor * np.random.normal(loc=0.0, scale=1.0, size=embedding1.shape)
        embedding2 += noise_factor * np.random.normal(loc=0.0, scale=1.0, size=embedding2.shape)

        # Prepare input
        input_features = np.hstack((embedding1, embedding2))

        # Predict
        probability = model.predict(input_features)[0][0]
        result = "Plagiarized" if probability > 0.5 else "Not Plagiarized"
        confidence = f"{probability * 100:.2f}%"

    return render_template('index.html', result=result, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
