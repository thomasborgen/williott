from google.cloud.texttospeech import (
    TextToSpeechClient,
    SsmlVoiceGender,
    AudioConfig,
    VoiceSelectionParams,
    AudioEncoding,
)


def speech_client() -> TextToSpeechClient:
    return TextToSpeechClient()


def speech_japanese_voice() -> VoiceSelectionParams:
    return VoiceSelectionParams(language_code="ja-JP", ssml_gender=SsmlVoiceGender.MALE)


def speech_english_voice() -> VoiceSelectionParams:
    return VoiceSelectionParams(language_code="en-US", ssml_gender=SsmlVoiceGender.MALE)


def speech_audio_config() -> AudioConfig:
    return AudioConfig(audio_encoding=AudioEncoding.MP3)
