from flask import Flask, jsonify, request
from Classifier import  get_prediction
import os, ssl
#if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
# ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context =ssl._create_unverified_contex
app = Flask(__name__)

@app.route("/predict-digit", methods=["POST"])
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("digit")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)