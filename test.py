import whisper
import os 


if os.path.exists("test.wav"):
    print("Arquivo encontrado. Continuando com a transcrição...")
else:
    print("Arquivo não encontrado. Verifique a gravação e o salvamento do arquivo.")
