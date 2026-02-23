"""
Emotion Detection Flask Application.

This module defines the web interface for analyzing text
and returning detected emotions using the emotion_detector function.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion() -> str:
    """
    Analyze user-provided text and return emotion analysis results.

    Returns:
        str: A formatted string containing emotion scores and
        the dominant emotion, or an error message if input is invalid.
    """
    text_to_analyse: str | None = request.args.get("textToAnalyze")

    response: dict = emotion_detector(text_to_analyse)
    dominant_emotion: str | None = response.get("dominant_emotion")

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')}, "
        f"'sadness': {response.get('sadness')}. "
        f"The dominant emotion is "
        f"{dominant_emotion}."
    )


@app.route("/")
def render_index_page() -> str:
    """
    Render the main page of the application.

    Returns:
        str: The rendered index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    