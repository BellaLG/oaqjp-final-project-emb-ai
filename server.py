from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detect():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Exception handling for blank or missing input
    if not text_to_analyze:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Invalid text! Please try again!'
        }), 400

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Format the response string
    formatted_response = format_emotion_response(response)

    # Return the formatted response as JSON with status 200
    return jsonify(formatted_response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
