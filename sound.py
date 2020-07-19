from gtts import gTTS
from playsound import playsound

text = input('Enter your text: ')
fie = input('Enter file you wanna save sound in: ')
audio = fie+'.mp3'
language = 'en'
sp = gTTS(text = text, lang= language, slow= True)

sp.save(audio)
playsound(audio)