# Proyecto-de-Final-IA
Karaoke con Inteligencia Artificial
## Nombre
Carlos Manuel Perdomo Zorrilla
## Matrícula
24-EISN-2-006
## Proyecto

🎤 Karaoke con Inteligencia Artificial

📌 Descripción

Este proyecto consiste en el desarrollo de un sistema de karaoke inteligente que utiliza técnicas de Inteligencia Artificial y Deep Learning para analizar canciones y evaluar el desempeño del usuario al cantar.

El sistema permite:

Separar la voz e instrumental de una canción
Transcribir automáticamente la letra
Analizar el canto del usuario
Generar una puntuación basada en similitud

🎯 Objetivos
Aplicar modelos de Deep Learning en procesamiento de audio
Desarrollar una aplicación interactiva
Evaluar el desempeño vocal de un usuario
Integrar múltiples tecnologías en un solo sistema

🧠 Tecnologías utilizadas
Python
Demucs → separación de voz e instrumental
Whisper → transcripción de audio
Librosa → extracción de características (MFCC)
NumPy → procesamiento numérico
SciPy → cálculo de similitud
Gradio → interfaz de usuario
FFmpeg → procesamiento de audio

⚙️ Instalación
Clonar el repositorio o descargar los archivos
Instalar dependencias:
pip install demucs openai-whisper gradio librosa numpy scipy ffmpeg-python
Instalar FFmpeg en el sistema (requerido)

🚀 Uso

Ejecutar la aplicación:

python app.py

Luego:

Subir una canción original
Subir la grabación del usuario
El sistema procesará y mostrará:
Letra detectada
Puntuación
Nivel de desempeño

🧪 Funcionamiento del sistema

El sistema trabaja en varias etapas:

Separación de audio

Se utiliza un modelo de Deep Learning para dividir la canción en:

Voz
Instrumental
Transcripción

Se aplica un modelo de reconocimiento de voz para obtener la letra de la canción.

Extracción de características

Se extraen características del audio (MFCC), que representan el contenido sonoro.

 Comparación

Se comparan las características del audio original y del usuario mediante una métrica de similitud.

Evaluación

Se genera una puntuación y una clasificación del desempeño del usuario.
