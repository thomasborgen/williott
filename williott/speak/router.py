from typing import Annotated
from fastapi import APIRouter, Path, Response, Depends, Query

from google.cloud import texttospeech

from google.cloud.texttospeech import (
    SynthesisInput,
    TextToSpeechClient,
    VoiceSelectionParams,
    AudioConfig,
)

from williott.speak.dependencies import (
    speech_audio_config,
    speech_client,
    speech_english_voice,
    speech_japanese_voice,
)


router = APIRouter(
    prefix="/speak",
    tags=["speak"],
    dependencies=[],
)


@router.get("/english/{text}")
async def read_english(
    text: Annotated[str, Path()],
    client: Annotated[TextToSpeechClient, Depends(speech_client)],
    voice: Annotated[VoiceSelectionParams, Depends(speech_english_voice)],
    audio_config: Annotated[AudioConfig, Depends(speech_audio_config)],
):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    speech = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return Response(content=speech.audio_content, media_type="audio/mpeg")


@router.get("/japanese/{text}")
async def read_japanese_old(
    text: Annotated[str, Path()],
    client: Annotated[TextToSpeechClient, Depends(speech_client)],
    voice: Annotated[VoiceSelectionParams, Depends(speech_japanese_voice)],
    audio_config: Annotated[AudioConfig, Depends(speech_audio_config)],
):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    speech = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return Response(content=speech.audio_content, media_type="audio/mpeg")


@router.get("")
async def read_japanese(
    text: Annotated[str, Query()],
    client: Annotated[TextToSpeechClient, Depends(speech_client)],
    voice: Annotated[VoiceSelectionParams, Depends(speech_japanese_voice)],
    audio_config: Annotated[AudioConfig, Depends(speech_audio_config)],
) -> None:
    synthesis_input = SynthesisInput(ssml=f"<speak>{text}</speak>")

    speech = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return Response(content=speech.audio_content, media_type="audio/mpeg")
