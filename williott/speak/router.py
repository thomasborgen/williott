from fastapi import APIRouter, Response

from google.cloud import texttospeech


router = APIRouter(
    prefix="/speak",
    tags=["speak"],
    dependencies=[],
)

# Instantiates a client
client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)


@router.get("/{text}")
async def read_item(text: str):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    speech = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return Response(content=speech.audio_content, media_type="audio/mpeg")