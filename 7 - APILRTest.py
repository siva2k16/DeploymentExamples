import requests

# Function to test the prediction API
def test_prediction_api():
    url = "http://127.0.0.1:5003/prediction/api/v1.0/some_prediction"
    params = {
        'f1': 2.5,
        'f2': 3.0,
        'f3': 4.0
    }
    response = requests.get(url, params=params)
    print("Predicted response:", response.text)

# Make sure your Flask app is running before executing this function
# test_prediction_api()
