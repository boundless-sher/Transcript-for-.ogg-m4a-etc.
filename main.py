import speech_recognition as sr
import pydub

import time
from os import path 

####    convert file into .wav file     #####
input_file_name = ""
output_file_name = ""
expected_format = ""


def get_path(file_name):
    return path.join(path.dirname(path.realpath(__file__)), file_name)

def get_inputs():
    global input_file_name, output_file_name, expected_format
    input_file_name = input('file name (example.mp3): ')
    expected_format = input('format you want the file to convert to: ')
    output_file_name = input('converted file name: ')

try:
    get_inputs()
    audio = pydub.AudioSegment.from_file(get_path(input_file_name))
    audio.export(get_path(output_file_name + "." + expected_format), format=expected_format)
except Exception as e:
    print(e)
    

####        get the transcript          #####  
r = sr.Recognizer()
with sr.AudioFile(get_path(output_file_name + '.' + expected_format)) as source:
    audio = r.record(source)

try:
    start_sphinx = time.time()
    print('sphinx thinks you said:', r.recognize_sphinx(audio))
    print('time sphinx took to transcript:', time.time() - start_sphinx)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

try:
    start_google = time.time()
    print('google thinks you said:', r.recognize_google(audio))
    print('time google took to transcript:', time.time() - start_google)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
