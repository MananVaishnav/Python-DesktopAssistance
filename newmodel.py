import pyttsx3 # text to speech library
import speech_recognition as spr


engine = pyttsx3.init('sapi5') # here espeak is TTS engine... more TTS engines : Sapi5, nssss
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # id 1 = female voice and 0 = male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# it take commands from user and return string output
def take_cmd():
    sr = spr.Recognizer()
    with spr.Microphone as source:
        print('Listening...')
        sr.pause_threshold = 1
        audio = sr.listen(source)

    try:
        print('Recognizing...')
        usr_query = sr.recognize_google_cloud(audio, language='en-IN')
        print(f'user said:{usr_query}')
    except Exception as e:
        # print(e)

        speak('sir say that again please')
        speak('sir say that again please')
        return 'None'
    return usr_query

if __name__ == "__main__":
    while True:
        query = take_cmd().lower()