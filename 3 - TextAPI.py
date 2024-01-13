from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    if 'text' in data:
        text = data['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return jsonify({
            'text': text,
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        }), 200
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
