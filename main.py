#!/usr/bin/env python3

import pyaudio
import wave
import time
import sys

import speech_recognition as speech

CHUNK = 1026
wf = wave.open('harvard.wav')
pa = pyaudio.PyAudio()

stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

recognizer = speech.Recognizer()
sample = speech.AudioFile('harvard.wav')

with sample as source:
  recognizer.adjust_for_ambient_noise(source, duration=1)
  audio = recognizer.record(source)

print(recognizer.recognize_google(audio))

while data != '':
  stream.write(data)
  data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

pa.terminate()

'''
print(speech.Microphone.list_microphone_names())

with mic as source:
    recognize.adjust_for_ambient_noise(source)
    audio = recognize.listen(source)

print(recognize.recognize_google(audio, show_all=True))
'''

'''
with sample as source:
    recognize.adjust_for_ambient_noise(source, duration=0.5)
    audio = recognize.record(source)

print(recognize.recognize_google(audio, show_all=True))
'''

'''
harvard = speech.AudioFile('harvard.wav')

with harvard as source:
    audio = recognize.record(source, offset=4.7, duration=2.8)

print(recognize.recognize_google(audio))
'''
