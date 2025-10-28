# Import the requests library to handle HTTP requests
import requests  
import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
   # URL of the emtotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }  
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the emotions from the response
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    
    #Getting the information for the emotions
    emotions = {
        'anger': emotion_data.get('anger', 0),
        'disgust': emotion_data.get('disgust', 0),
        'fear': emotion_data.get('fear', 0),
        'joy': emotion_data.get('joy', 0),
        'sadness': emotion_data.get('sadness', 0)
    }

    #return the max_emotion
    dominant_emotion = max(emotions, key=emotions.get)
   
    # Add dominant emotion to the output dictionary
    emotions['dominant_emotion'] = dominant_emotion

    # Print the emotions in a list with the dominant_emotion
    return emotions

#print the formatted string
def format_emotion_response(emotions):
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
    )
    return {'response': response_str}
