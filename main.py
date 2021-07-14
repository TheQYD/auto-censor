#!/usr/bin/env python3

import speech_recognition as speech

recognize = speech.Recognizer()
sample = speech.AudioFile('harvard.wav')

with sample as source:
    recognize.adjust_for_ambient_noise(source, duration=0.5)
    audio = recognize.record(source)

print(recognize.recognize_google(audio, show_all=True))


'''
harvard = speech.AudioFile('harvard.wav')

with harvard as source:
    audio = recognize.record(source, offset=4.7, duration=2.8)

print(recognize.recognize_google(audio))
'''
