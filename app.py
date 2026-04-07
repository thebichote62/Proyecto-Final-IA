import gradio as gr
from separar import separar_audio
from transcribir import transcribir_audio
from evaluar import comparar_audios, puntuacion

def procesar(audio_original, audio_usuario):
    # Separar audio
    separar_audio(audio_original)

    # Transcribir letra
    texto = transcribir_audio(audio_original)

    # Evaluar canto
    sim = comparar_audios(audio_original, audio_usuario)
    score, nivel = puntuacion(sim)

    resultado = f"""
    🎤 RESULTADO DEL KARAOKE

    📝 Letra detectada:
    {texto}

    ⭐ Puntuación: {score:.2f}
    📊 Nivel: {nivel}
    """

    return resultado

gr.Interface(
    fn=procesar,
    inputs=[
        gr.Audio(type="filepath", label="Canción original"),
        gr.Audio(type="filepath", label="Tu canto")
    ],
    outputs="text",
    title="Karaoke con IA 🎤",
    description="Sube una canción y canta para evaluarte con Inteligencia Artificial"
).launch()