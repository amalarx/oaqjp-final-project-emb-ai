"""Unit tests for the Watson NLP emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check formatting, dominant emotions and error handling."""

    def check_dominant(self, emotion):
        """Simulate Watson's reply and check the selected emotion."""
        scores = {key: 0.05 for key in (
            "anger", "disgust", "fear", "joy", "sadness"
        )}
        scores[emotion] = 0.9
        mocked_response = Mock(status_code=200)
        mocked_response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        with patch("EmotionDetection.emotion_detection.requests.post",
                   return_value=mocked_response):
            result = emotion_detector(f"Example of {emotion}")
        self.assertEqual(result["dominant_emotion"], emotion)
        for key, value in scores.items():
            self.assertEqual(result[key], value)

    def test_joy(self):
        """Joy is selected when it has the highest score."""
        self.check_dominant("joy")

    def test_anger(self):
        """Anger is selected when it has the highest score."""
        self.check_dominant("anger")

    def test_disgust(self):
        """Disgust is selected when it has the highest score."""
        self.check_dominant("disgust")

    def test_sadness(self):
        """Sadness is selected when it has the highest score."""
        self.check_dominant("sadness")

    def test_fear(self):
        """Fear is selected when it has the highest score."""
        self.check_dominant("fear")

    def test_blank_input(self):
        """Blank text is handled without calling Watson."""
        with patch("EmotionDetection.emotion_detection.requests.post") as post:
            result = emotion_detector(" ")
        self.assertIsNone(result["dominant_emotion"])
        post.assert_not_called()

    def test_watson_bad_request(self):
        """HTTP 400 results in the expected empty output."""
        with patch("EmotionDetection.emotion_detection.requests.post",
                   return_value=Mock(status_code=400)):
            result = emotion_detector("invalid")
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()
