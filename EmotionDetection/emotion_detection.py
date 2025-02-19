import json, requests

def emotion_detector(text_to_analyze):

    # construct a post request to watson sentiment analyzer with the text to analyze
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)

    # process the response
    formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    formatted_response['dominant_emotion'] = dominant_emotion
    return formatted_response