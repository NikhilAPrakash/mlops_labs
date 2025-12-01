from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__, static_folder='statics')

# Load the TensorFlow model trained on the Wine dataset
model = tf.keras.models.load_model('my_model.keras')

# Wine dataset has 3 classes: 0, 1, 2
class_labels = ['class_0', 'class_1', 'class_2']


@app.route('/')
def home():
    return "Welcome to the Wine Classifier API!"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form

            # Expect 13 features: feature1 ... feature13
            features = []
            for i in range(1, 14):
                value = float(data[f'feature{i}'])
                features.append(value)

            input_data = np.array(features)[np.newaxis, :]

            prediction = model.predict(input_data)
            predicted_class_idx = int(np.argmax(prediction))
            predicted_class = class_labels[predicted_class_idx]

            return jsonify({"predicted_class": predicted_class})
        except Exception as e:
            return jsonify({"error": str(e)})
    elif request.method == 'GET':
        return render_template('predict.html')
    else:
        return "Unsupported HTTP method"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
