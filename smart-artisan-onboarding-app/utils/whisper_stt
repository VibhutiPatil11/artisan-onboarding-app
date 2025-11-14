import openai

def speech_to_text(audio_bytes):
    result = openai.audio.transcriptions.create(
        file=("audio.wav", audio_bytes),
        model="whisper-1"
    )
    return result.text
