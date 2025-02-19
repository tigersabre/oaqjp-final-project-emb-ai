# import flask requirements
from flask import Flask, render_template, request

# import emotion detector library
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    e_analysis = emotion_detector(text_to_analyze)

    return f"""
            For the given statement, the system response is 'anger': {e_analysis['anger']}, 
            'disgust': {e_analysis['disgust']}, 'fear': {e_analysis['fear']}, 
            'joy': {e_analysis['joy']}, and 'sadness': {e_analysis['sadness']}. 
            The dominant emotion is {e_analysis['dominant_emotion']}."
            """

@app.route('/')
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)