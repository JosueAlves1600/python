import sounddevice as sd
import numpy as np
import whisper
import tempfile
import scipy.io.wavfile as wav

DURACAO = 10
TAXA_AMOSTRAGEM = 44100

print("Gravando o áudio que está sendo reproduzido no PC...")
gravacao = sd.rec(int(DURACAO * TAXA_AMOSTRAGEM), samplerate=TAXA_AMOSTRAGEM,channels=2, dtype='int16')
sd.wait()
print(" Terminou de gravar")

arquivo_temp = tempfile.mktemp(suffix=".wav")
wav.white(arquivo_temp, TAXA_AMOSTRAGEM, gravacao)

print(" Transcrevendo com Whisper...")
modelo = whisper.load_model("base")
resultado = modelo.transcribe(arquivo_temp, language="pt")

print("\n Transcrição:")
print(resultado["text"])