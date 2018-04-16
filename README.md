#charly

#gestion des evenements programmés par un cron ?


#install dep

apt-get update

apt-get upgrade -y

#to allow charly to speak

sudo apt-get install libttspico-utils

#speech recognition library (>=3.5

pip install SpeechRecognition

#to use microphone

apt-get install python-all-dev

apt-get install portaudio19-dev

pip install PyAudio

#launch charly

python3 charly.py
