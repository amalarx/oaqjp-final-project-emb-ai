"""Detect emotions in text using IBM Watson NLP."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the most dominant emotion."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {**dict.fromkeys(EMOTIONS), "dominant_emotion": None}

    response = requests.post(
        WATSON_URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=20,
    )
    if response.status_code == 400:
        return {**dict.fromkeys(EMOTIONS), "dominant_emotion": None}
    response.raise_for_status()
    scores = response.json()["emotionPredictions"][0]["emotion"]
    output = {emotion: scores[emotion] for emotion in EMOTIONS}
    output["dominant_emotion"] = max(output, key=output.get)
    return output
