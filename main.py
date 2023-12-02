import whisper
import pyaudio
import requests
import json
import pyaudio
import wave
import os
from elevenlabs import set_api_key
from elevenlabs import clone, generate, voices, play
from dotenv import load_dotenv
from PIL import Image, ImageTk
import threading
from tkinter import Tk,Button, PhotoImage, Label

load_dotenv()
set_api_key(os.environ["ELEVEN_LABS_KEY"])
api_url = os.environ["api_url"]
api_key = os.environ["api_key"]
waveSalida = "G_Temp.wav"

model = whisper.load_model("small")


voices = voices()
Voz = voices[-1]

def GrabarAudio():
    """Esta funcion grava el audio del microfono
    """
    audio = pyaudio.PyAudio()

    stream = audio.open(format = pyaudio.paInt16, channels = 1, rate = 44100,
                        input = True, frames_per_buffer = 1024)
    
    print("Grabando")
    frames=[]

    for i in range(0, int(44100 / 1024 * 7)):
        data = stream.read(1024)
        frames.append(data)
    
    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("Grabacion terminada")
    #Se guarda lo grabado en formato wav

    waveF = wave.open(waveSalida, 'wb')
    waveF.setnchannels(1)
    waveF.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveF.setframerate(44100)
    waveF.writeframes(b''.join(frames))
    waveF.close()


def DeAudioatTexto(audioF : str) -> str:
    """Esta funcion devuelve un texto de un archivo de audio utilizando whisper

    Args:
        audioF (str): path del audio

    Returns:
        str: Transcripcion
    """
    result = model.transcribe(audioF)
    return result["text"]


def Comandos():
    """Esta funcion se encarga de llamar a las otras cuando se necesitan
    """
    GrabarAudio()
    Comando = DeAudioatTexto(waveSalida)
    Comando = Comando.lower()
    print(Comando)
    os.remove(waveSalida)
    if 'hola' in Comando and 'laura' in Comando:
        EnviarAChatGpt('Saluda de manera formal, presentandote como LAURA, un asistente virtual potenciado por inteligencia artificial.')
    else:
        EnviarAChatGpt(Comando)

def EnviarAChatGpt(prompt:str):
    """Esta funcion manda una peticion ala api de chatgpt

    Args:
        prompt (str): Texto a predecir
    """
    data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}]
    }

    headers = {'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'}

    # Realiza la solicitud utilizando la biblioteca 'requests'
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    response_data = response.json()

    assistant_message = response_data['choices'][0]['message']
    print(f"Respuesta: {assistant_message['content']}")
    audio = generate(text=assistant_message['content'], voice=Voz, model='eleven_multilingual_v1')

    play(audio)

class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        """
        Método llamado al cerrar la ventana principal.

        Cierra la ventana principal utilizando el método quit() de Tkinter,
        lo que resulta en la terminación del programa.
        """
        self.root.quit()
    
    def run(self):
        root = Tk()
        root.geometry('500x600')
        root.title('L.A.U.R.A')
        Foto = Image.open("imgs\personaje.jpg")
        Foto = Foto.resize((400, 400), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(Foto)

        label1 = Label(image=test)
        label1.image = test
        label1.place(x=60,y=0)
        microphone_img = PhotoImage(file=r'imgs/microphone.png')
        microphone_img = microphone_img.subsample(4,4)
        btn_micro = Button(root,text='Click me',image=microphone_img,command=Comandos)
        btn_micro.place(x=200,y=425)
        root.mainloop()

if __name__ == '__main__':
    app = App()