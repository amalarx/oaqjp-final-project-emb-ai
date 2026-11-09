# Emotion Detector — IBM Watson NLP Final Project

An AI-based English emotion detection web application for the IBM/Coursera *Developing AI Applications with Python and Flask* final project.

The application uses Watson NLP EmotionPredict to calculate anger, disgust, fear, joy, and sadness scores and return the dominant emotion.

## Project files

- `EmotionDetection/emotion_detection.py` — Watson NLP API integration and HTTP 400 handling.
- `EmotionDetection/__init__.py` — Python package.
- `server.py` — Flask application and blank input error handling.
- `test_emotion_detection.py` — 7 unit tests with mocked Watson responses.
- `templates/index.html`, `static/` — browser interface.

## Run

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_emotion_detection
python server.py
```

Visit http://localhost:5000.

## Static analysis

```bash
pylint server.py
```

**Note:** Watson endpoint `sn-watson-emotion.labs.skills.network` may only work from the IBM Skills Network environment. Mocked unit tests do not confirm live Watson availability; test deployment inside the course lab before taking screenshots.
