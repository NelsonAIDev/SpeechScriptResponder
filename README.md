##<h1>L.A.U.R.A - Asistente Virtual Potenciado por Inteligencia Artificial</h1><br>
<p>L.A.U.R.A (Linguistically Advanced and User-friendly Robotic Assistant) es un asistente virtual desarrollado utilizando tecnologías de inteligencia artificial. Puede realizar tareas como transcripción de voz, interacción con el modelo GPT-3.5 Turbo de OpenAI para respuestas conversacionales y generar mensajes de voz utilizando la API de Eleven Labs.<p>
<br>
##<h1>Requisitos</h1>
Asegúrate de tener instaladas las siguientes bibliotecas y módulos de Python:

aiohttp==3.8.4
aiosignal==1.3.1
asttokens==2.2.1
async-timeout==4.0.2
attrs==23.1.0
backcall==0.2.0
certifi==2023.5.7
charset-normalizer==3.1.0
colorama==0.4.6
decorator==5.1.1
elevenlabs==0.2.12
executing==1.2.0
ffmpeg-python==0.2.0
filelock==3.12.0
frozenlist==1.3.3
future==0.18.3
idna==3.4
ipython==8.13.2
jedi==0.18.2
Jinja2==3.1.2
llvmlite==0.40.0
MarkupSafe==2.1.2
matplotlib-inline==0.1.6
more-itertools==9.1.0
mpmath==1.3.0
multidict==6.0.4
networkx==3.1
numba==0.57.0
numpy==1.24.3
openai==0.27.6
openai-whisper==20230314
opencv-python==4.7.0.72
parso==0.8.3
pickleshare==0.7.5
Pillow==9.5.0
prompt-toolkit==3.0.38
pure-eval==0.2.2
PyAudio==0.2.13
pydantic==1.10.7
Pygments==2.15.1
python-dotenv==1.0.0
regex==2023.5.5
requests==2.30.0
semantic-version==2.10.0
setuptools-rust==1.6.0
six==1.16.0
stack-data==0.6.2
sympy==1.12
tiktoken==0.3.1
torch==2.0.1
tqdm==4.65.0
traitlets==5.9.0
typing_extensions==4.5.0
urllib3==2.0.2
Wave==0.0.2
wcwidth==0.2.6
yarl==1.9.2

Además, necesitarás una clave de API de Eleven Labs y configurar las variables de entorno. Consulta la documentación de Eleven Labs para obtener más información.

Uso
Ejecuta el script main.py para iniciar L.A.U.R.A.

La interfaz de usuario mostrará una imagen del personaje y un botón con un ícono de micrófono.

Haz clic en el botón de micrófono y pronuncia tus comandos.

L.A.U.R.A grabará tu voz, transcribirá el comando y enviará la solicitud al modelo GPT-3.5 Turbo para obtener una respuesta.

La respuesta se convertirá en un mensaje de voz generado por la API de Eleven Labs y se reproducirá.

Personalización
Puedes personalizar la apariencia de la interfaz de usuario cambiando la imagen del personaje (imgs/personaje.jpg) y el ícono del micrófono (imgs/microphone.png).

Notas
Asegúrate de tener una conexión a Internet activa para interactuar con la API de Eleven Labs y la API de OpenAI.

Si experimentas problemas de audio, verifica la configuración de tu micrófono y altavoces.

Ten en cuenta que este proyecto es un ejemplo básico y puede requerir ajustes según tus necesidades y preferencias.

¡Disfruta interactuando con L.A.U.R.A, tu asistente virtual inteligente!