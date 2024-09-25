import os
import subprocess

# Carpetas de entrada y salida
input_folder = 'videos'
output_folder = 'videos_convertidos'

# Asegurarse de que la carpeta de salida exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Función para convertir y comprimir videos
def convert_video(input_path, output_path):
    command = [
        'ffmpeg',
        '-i', input_path,            # Archivo de entrada
        '-c:v', 'libvpx-vp9',        # Códec de video VP9 para WebM
        '-b:v', '1M',                # Bitrate de video (ajusta si necesitas más o menos compresión)
        '-c:a', 'libopus',           # Códec de audio Opus
        output_path
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Convertido: {input_path} -> {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir {input_path}: {e}")

# Procesar todos los archivos MP4 en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webm')
        convert_video(input_path, output_path)

print("Conversión completada.")
