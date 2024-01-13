import requests

def test_sentiment_analysis():
    url = "http://127.0.0.1:5000/sentiment"

    # Example of a valid request with text for sentiment analysis
    valid_data = {
        "text": "I love this product! It's amazing."
    }

    valid_response = requests.post(url, json=valid_data)
    print("Valid request response:", valid_response.json())

    # Example of an invalid request without text
    invalid_data = {}

    invalid_response = requests.post(url, json=invalid_data)
    print("Invalid request response:", invalid_response.json())

# Make sure your Flask app is running before executing this function
# test_sentiment_analysis()
