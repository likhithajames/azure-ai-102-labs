from dotenv import load_dotenv
from datetime import datetime

import os
import azure.cognitiveservices.speech as speech_sdk

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    print('Speak now...')

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command

def getDay():
    now = datetime.now().strftime("%A")
    response_text = 'Today is {}'.format(now)

    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-LibbyNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    
    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)
    
    # Synthesize spoken output
    speech_config.speech_synthesis_voice_name = "ml-IN-SobhanaNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    ssml = """
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='ml-IN'>
        <voice name='ml-IN-SobhanaNeural'>
            ഒരു നല്ല ദിനം ആശംസിക്കുന്നു.
        </voice>
    </speak>
    """
    speak = speech_synthesizer.speak_ssml_async(ssml).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

try:
    global speech_config

    # Get Configuration Settings
    load_dotenv()
    cog_key = os.getenv('KEY')
    cog_region = os.getenv('REGION')

    # Configure speech service
    speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
    print('Ready to use speech service in:', speech_config.region)

    # Get spoken input
    command = TranscribeCommand()
    if command.lower() == 'what day is today?':
        getDay()

except Exception as ex:
    print(ex)

