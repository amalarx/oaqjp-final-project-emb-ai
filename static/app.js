const input = document.getElementById('textToAnalyze');
const result = document.getElementById('result');
document.getElementById('analyze').addEventListener('click', async () => {
  result.textContent = 'Analyzing...';
  try {
    const response = await fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(input.value)}`);
    result.textContent = await response.text();
  } catch (error) {
    result.textContent = 'Unable to connect to the emotion detection service.';
  }
});
