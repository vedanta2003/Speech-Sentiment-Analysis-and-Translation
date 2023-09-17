from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

recognizer=sr.Recognizer ()

with sr.Microphone() as source:
    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for your message...')
    recordedaudio=recognizer. listen (source)
    print('Done recording..')

try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio, language= 'en-US')
    print( 'Your message:{}'.format (text))

except Exception as ex:
    print (ex)

#translation
from googletrans import Translator

def translate_hindi_to_english(text):
   translator = Translator()
   translated_text = translator.translate(text, src='hi', dest='en')
   return translated_text.text


english_translation = translate_hindi_to_english(text)
print("Hindi: ", text)
print("English: ", english_translation)

#Sentiment analysis

Sentence=[str (text)]
analyser=SentimentIntensityAnalyzer()

for i in Sentence:
    v=analyser.polarity_scores(i)
    print(v)

