from dotenv import load_dotenv
from datetime import datetime

import os
import azure.cognitiveservices.speech as speech_sdk

def Translate(target_language):
    translation= ''

    #Translate the speech
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)
    print('Speak now...')
    translation_result = speech_recognizer.recognize_once_async().get()
    print('Translating {} to malayalam'.format(translation_result.text))
    translation = translation_result.translations[target_language]
    print(translation)

    #synthesize the translated text
    speech_config.speech_synthesis_voice_name = "ml-IN-SobhanaNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    speak = speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

try:
    load_dotenv()
    
    endpoint = os.getenv("ENDPOINT")
    key = os.getenv("KEY")
    region = os.getenv("REGION")
    
    #configuration - translation
    speech_translation_config = speech_sdk.translation.SpeechTranslationConfig(subscription=key, region=region)
    speech_translation_config.speech_recognition_language = "en-US"
    speech_translation_config.add_target_language("ml") 

    #configuration - speech
    speech_config = speech_sdk.SpeechConfig(subscription=key, region=region)

    #translate the speech
    Translate("ml")

except Exception as err:
    print(f"Encountered exception. {err}")