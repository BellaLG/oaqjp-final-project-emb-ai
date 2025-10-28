"""Flask web application for emotion detection using IBM Watson API."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector, format_emotion_response

# Create Flask application instance
app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detect():
    """
    Handle GET requests for emotion detection.

    Retrieves the text from query parameters, analyzes emotions
    using the emotion_detector() function, and returns the result
    in JSON format or an error message if no dominant emotion is found.
    """
    # Retrieve and clean the text to analyze
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Handle invalid or empty input
    if response.get("dominant_emotion") is None:
        return jsonify( "Invalid text! Please try again!"), 200
    # Format and return the response
    formatted_response = format_emotion_response(response)
    return  formatted_response, 200


@app.route("/")
def home():
    """
    Render the home page with the input form.
    """
    return render_template("index.html")


if __name__ == "__main__":
    # Run Flask application on all network interfaces
    app.run(host="0.0.0.0", port=5000)
