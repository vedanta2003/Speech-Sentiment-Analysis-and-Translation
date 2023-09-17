

# Speech Sentiment Analysis and Translation

This Python script allows you to perform sentiment analysis and translation on spoken text using various libraries and APIs. It's divided into three main sections: audio recording, translation, and sentiment analysis.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Dependencies

Before running this code, you need to install the following Python libraries:

- [vaderSentiment](https://pypi.org/project/vaderSentiment/): A library for sentiment analysis.
- [speech_recognition](https://pypi.org/project/SpeechRecognition/): For audio recording and speech recognition.
- [googletrans](https://pypi.org/project/googletrans/): To perform text translation.

You can install these libraries using pip:

```bash
pip install vaderSentiment
pip install SpeechRecognition
pip install googletrans==4.0.0-rc1
```

## Installation

1. Clone or download this repository to your local machine.

2. Make sure you have the required dependencies installed (see the Dependencies section above).

## Usage

1. Run the script using Python:

```bash
python speech_sentiment_translation.py
```

2. Follow the on-screen instructions:
   - The script will clear background noise for a second.
   - It will then wait for you to speak a message.
   - After recording, it will attempt to recognize your speech and print the recognized message in English.

3. If the recognition is successful, it will:
   - Translate the recognized text from Hindi to English.
   - Perform sentiment analysis on the translated text and print the sentiment scores.

## How It Works

1. **Audio Recording**: The code uses the `speech_recognition` library to record audio from your microphone. It adjusts for ambient noise and then waits for your message.

2. **Speech Recognition**: It uses Google's speech recognition API to convert the recorded audio into text. The recognized text is printed on the screen.

3. **Translation**: The script translates the recognized text from Hindi to English using the `googletrans` library. The translation is printed both in Hindi and English.

4. **Sentiment Analysis**: It performs sentiment analysis on the translated text using the VADER sentiment analysis tool from the `vaderSentiment` library. The sentiment scores (positive, negative, neutral, and compound) are printed on the screen.

## License

This code is provided under the [MIT License](LICENSE). Feel free to modify and use it in your projects.

---

Make sure to include the relevant links, license, and any additional information specific to your use case or project.
