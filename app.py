# app.py
import xgboost as xgb
import numpy as np
import pickle
from flask import Flask, request, jsonify
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time
from prometheus_flask_exporter import PrometheusMetrics

# Load your trained XGBoost model
with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)


def your_model_function(input_data):
    try:
        # Assuming input_data is a list of features
        input_array = np.array([input_data])
        #dmatrix = xgb.DMatrix(input_array)

        # Make predictions
        predictions = model.predict(input_array)

        # Assuming a binary classification, adjust as needed
        if predictions[0]==0 :
            result = "setosa"
        elif predictions[0]==1 :
            result = "versicolor"
        else :
            result = "virginica"
        #result = 'Positive' if predictions[0] > 0.5 else 'Negative'
        return result

    except Exception as e:
        return str(e)




app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)

metrics = PrometheusMetrics(app)

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    REQUEST_COUNT.labels('POST', '/predict', 200).inc()
    try:
        data = request.get_json(force=True)
        input_data = data['input']  # adjust based on your model's input format
        result = your_model_function(input_data)
        response = {'result': result}
        REQUEST_LATENCY.labels('POST', '/predict').observe(time.time() - start_time)
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)