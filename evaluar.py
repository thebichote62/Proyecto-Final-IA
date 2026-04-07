import librosa
import numpy as np
from scipy.spatial.distance import cosine

def extraer_features(ruta_audio):
    y, sr = librosa.load(ruta_audio)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)

def comparar_audios(audio_original, audio_usuario):
    f1 = extraer_features(audio_original)
    f2 = extraer_features(audio_usuario)
    similitud = 1 - cosine(f1, f2)
    return similitud

def puntuacion(similitud):
    score = similitud * 100

    if score > 85:
        nivel = "🔥 Excelente"
    elif score > 70:
        nivel = "👏 Bueno"
    elif score > 50:
        nivel = "🙂 Regular"
    else:
        nivel = "😅 Necesita práctica"

    return score, nivel