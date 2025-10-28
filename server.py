from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import format_emotion_response

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_detect():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        #format the response
        formatted_response = format_emotion_response(response)
        
    # If the response status code is 400, set response to None
    elif response.status_code == 500:
        formatted_response = None

    #return formatted response
    return formatted_response

@app.route("/") 
def home():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)

