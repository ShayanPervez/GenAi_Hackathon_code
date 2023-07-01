import os
import time
from gtts import gTTS
import speech_recognition as sr
import pydub.playback as playback
from pydub import AudioSegment


def speak(text):
    tts = gTTS(text=text)
    filename = "voice.mp3"
    tts.save(filename)
    audio = AudioSegment.from_file(filename, format="mp3")
    playback.play(audio)

def speak_hindi(text):
    tts = gTTS(text=text, lang='hi')
    filename = "voice_hindi.mp3"
    tts.save(filename)
    audio = AudioSegment.from_file(filename, format="mp3")
    playback.play(audio)

def speak_urdu(text):
    tts = gTTS(text=text, lang='ur')
    filename = "voice_ur.mp3"
    tts.save(filename)
    audio = AudioSegment.from_file(filename, format="mp3")
    playback.play(audio)


def get_audio():
    r = sr.Recognizer()
    said = ""
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.1)
            audio = r.listen(source)
            said = r.recognize_google(audio)
            said = said.lower()
            # print(f"Recognised: {said}")
    except Exception as e:
        return f"No input given {str(e)}"

    return said



# speak("I can help you with translation, reading books and can be your chatbot")
# speak("How can I help you with my services")
# get_audio()
# # speak("Because you did not speak anything we are closing our chat with you. Thankyou! please restart me to talk agai.")
# speak_hindi("मेज पर एक किताब है")
# speak_urdu("میں آپ کی مدد کرنے کے لئے یہاں ہوں۔")
