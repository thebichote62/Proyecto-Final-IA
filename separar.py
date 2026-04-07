import os

def separar_audio(ruta_audio):
    os.system(f"demucs {ruta_audio}")
    return "ok"