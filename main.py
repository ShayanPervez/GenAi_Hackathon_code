from PyPDF2 import PdfReader
from gtts import gTTS
import playsound
import speech_recognition as sr
import speech_to_text
import translation

def pdf_to_speech(file_path):
    with open(file_path,'rb') as file:
        pdf = PdfReader(file)

        #Extract text from each page
        text = ''
        for page in pdf.pages:
            text+= page.extract_text()
        print(text)
        speech_to_text.speak(text)
        print("Translating....")
        translated_text = translation.sentence_translation_mbart(text)
        print(translated_text)
        speech_to_text.speak_hindi(translated_text)


pdf_path = r'C:/Users/shpe1/Downloads/pdf-test.pdf'
outputs = pdf_to_speech(pdf_path)
print(outputs)
# speech_to_text.speak('name is',audio_file_name)

