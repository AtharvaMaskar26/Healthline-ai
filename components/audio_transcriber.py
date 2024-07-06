from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI()  

# This function starts recording when you press spacebar and stops recording when you release the spacebar.
def transcribe_audio(audio_file_url: str) -> str:
    """
    Description:
        - This function takes the audio file path and returns the transcriptions
    
    parameters:
        - audio_file_url (str): path of the audio file.

    returns:
        - transcript (str): Transcript generated using WhisperAPIs        
    """

    audio_file = open(audio_file_url, 'rb')

    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    return transcription.text