import whisper

model = whisper.load_model("base")

def transcribir_audio(ruta_audio):
    resultado = model.transcribe(ruta_audio)
    return resultado["text"]