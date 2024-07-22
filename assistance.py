from cProfile import label
import operator
import subprocess
import sys
import time
# from typing_extensions import Self
# from typing_extensions import Self
from pytube import YouTube
import pywhatkit
# import pywikihow
from pywikihow import search_wikihow
from twilio.rest import Client
import PyPDF2
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia 
import os
import webbrowser
import random
from requests import get
import pywhatkit as kit
import sys
import smtplib
import instaloader
import pyjokes
from bs4 import BeautifulSoup
import psutil
import speedtest
import json
import os.path
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from projectGUI import Ui_MainWindow
import openpyxl
# import urllib.request



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# it takes microphone input from the user


def news():
    main_url = 'https://newsapi.org/v2/everything?q=apple&from=2022-08-26&to=2022-08-26&sortBy=popularity&apiKey' \
               '=ed000a1dbbe348eea3d1d337e856056b '

    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def send_email(to, subject, content):
    sender_email = open("email.text", 'r').read()
    password = open("password.txt", 'r').read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    message = f'subject: {subject}\n\n {content}'
    server.sendmail(sender_email, to, message)
    server.close()

def pdf_reader():
    # book = open('python.pdf', 'rb')
    # pdfReader = PyPDF2.PdfFileReader(book)
    # pages = pdfReader.numPages
    speak("sir enter the name of the book which you want to read")
    n = input('Enter the book name')
    n = n.strip()+".pdf"
    book_n = open(n, 'rb')
    pdfreader = PyPDF2.PdfFileReader(book_n)
    pages = pdfreader.numPages
    speak(f'total number of pages in this book is {pages}')
    speak('sir tell me the page number i have to read')
    pgn = int(input('sir please enter the page number:-'))
    page = pdfreader.getPage(pgn)
    text = page.extractText()
    speak(text)

def wishme():
            hour = int(datetime.datetime.now().hour)
            tt = time.strftime("%I:%M %p")
            if 0 <= hour <= 12:
                print(f"good morning sir,its {tt}")
                speak(f"good morning sir,its {tt}")

            elif 12 <= hour < 18:
                print(f"good afternoon sir,its {tt}")
                speak(f"good afternoon sir,its {tt}")

            elif 18 <= hour < 22:
                speak(f"good evening sir,its {tt}")

            else:
                speak("good night sir!")

            print("Sir how can i help you??")
            speak("Sir how can i help you??")

            

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
               
    
    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")

        except Exception as e:
                # print(e)
            print("sir say that again please ")
            speak("sir say that again please!")
            return "None"
        query = query.lower()
        return query

    

    def TaskExecution(self):
        wishme()
        
        while True:

            self.query = self.take_command()

            if 'wikipedia' in self.query:
                speak("searching Wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia...")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("opening youtube sir")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("sir, what should i search on google?")
                cm = self.take_command()
                webbrowser.open(f"{cm}")

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                print(ip)
                speak(f"your IP address is {ip}")

            elif 'open github' in self.query:
                webbrowser.open("github.com")

            elif 'open notepad' in self.query:
                path1 = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(path1)
            elif 'close notepad' in self.query:  # for closing notepad
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")  # closing an application

            elif 'open zoom meeting' in self.query:
                speak('Opening zoom meeting app')
                filepath2 = "C:\\Users\\Manan V. Vaishnav\\AppData\\Roaming\\Zoom\\bin_00\\Zoom.exe"
                os.startfile(filepath2)
                speak('Sir what can i do now?')
                condition2 = self.take_command()
                if 'start a new meeting' in condition2:
                    pyautogui.run('New Meeting')
            #     if 'join new meeting' in self.query:
            # elif 'switch the window' in self.query:
            #     speak("okay sir i am switching the window")
            #     pyautogui.keyDown('alt')
            #     pyautogui.press('tab')
            #     time.sleep(1)
            #     pyautogui.keyUp('alt')

            # # elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
            #     speak('sir please enter username')
            #     name = input('enter user name:-')
            #     webbrowser.open(f'www.instagram.com/{name}')
            #     speak(f'sir hear is the profile of the user {name}')
            #     time.sleep(5)
            #     speak('sir would you like to download  profile pic of this account?')
            #     condition = self.take_command()
            #     if 'yes' in condition:
            #         mod = instaloader.Instaloader()
            #         mod.download_profile(name, profile_pic_only=True)
            #         speak('i am done sir...')
            #     else:
            #         pass

            elif "open hotstar" in self.query:
                speak("opening your disney plus hotstar")
                webbrowser.open("https://www.hotstar.com/in")

            elif "open gmail" in self.query:
                speak("opening your google mail")
                webbrowser.open("https://mail.google.com/mail/")

            elif "open google maps" in self.query:
                speak("opening google maps")
                webbrowser.open("https://www.google.co.in/maps/")

            elif "open calender" in self.query:
                speak("opening google calender")
                webbrowser.open("https://www.google.com/calendar/about/")

            elif 'open command prompt' in self.query:
                os.system('start cmd')

            elif "open whatsapp" in self.query:
                speak("opening your whatsapp...")
                webbrowser.open("https://web.whatsapp.com/")

            # elif 'send message' in self.query:
            #     kit.sendwhatmsg("+916353473828", "hey bro, how are you?", 1, 2)

            elif 'latest news' in self.query:
                speak('please wait sir, fetching the latest news')
                news()

            elif 'play music' in self.query:
                music_dir = "C:\\songs"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)  # for play random music
                for song in songs:  # for only play mp3 songs
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, rd))

            # for telling a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke('en')
                speak(joke)

            elif "send message" in self.query:
                kit.sendwhatmsg("+916353473828", "how are you?", 2, 25)

            # for shutdown,reset and sleep the system
            elif "log off" in self.query:
                speak("okay sir logging off the system")
                # os.system("shutdown /s /t 5")
                subprocess.call(["shutdown", "/l"])

            elif "shutdown the system" in self.query:
                #  os.system("shutdown /s /t 5")
                speak("hold on a second! your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif "restart the system" in self.query:
                # os.system("rund1132.exe powrprof.dll,  SetSuspendState 0,1,0")
                subprocess.call(["shutdown", "/r"])

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"sir, the time is {strTime}")

            elif 'switch the window' in self.query:
                speak("okay sir i am switching the window")
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')  # pyautoGUI lets Python control the mouse & keyboard, and other GUI automation task

            elif "send email" in self.query:
                try:
                    speak("what should i say")
                    content = self.take_command()
                    to = open("email.text", 'r').read()
                    speak("what is the subject for your mail")
                    subject = self.take_command()
                    send_email(to, subject, content)
                    speak("email has been sent successfully")
                except Exception as e:
                    speak("sorry sir i am not be able to send email")

            elif 'play a song' in self.query:
                print("sir can you please say the name of the song")
                speak("sir can you please say the name of the song")
                song = self.take_command()
                if 'play' in self.query:
                    song1 = song.replace("play", "")
                    speak("playing" + song)
                    print(f'playing{song}')
                    kit.playonyt(song)
                    print("playing")

            elif 'download video' in self.query:
                print("please enter the youtube video link you want to download")
                speak("please enter the youtube video link you want to download")
                link = input("Enter the youtube video link:- ")
                yt = YouTube(link)
                yt.streams.get_highest_resolution().download()
                print(f"sir downloaded {yt.title} from the link you given into the main folder")
                speak(f"sir downloaded {yt.title} from the link you given into the main folder")

            elif 'activate how to do mod' in self.query:
                print('how to  do mod is activated please tell me what you want to know')
                speak('how to  do mod is activated please tell me what you want to know')
                how = self.take_command()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            elif 'where we are' in self.query or 'where i am' in self.query:
                speak('wait sir, let me check')
                try:
                    ipaddr = requests.get('https://api.ipify.org').text
                    print(ipaddr)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipaddr + '.jason'
                    geo_requestes = requests.get(url)
                    geo_data = geo_requestes.jason()
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f'sir we are in {city} city of {state} state in {country}')

                except Exception as e:
                    speak('sorry sir, due to network issue i am not be able to find where we are')
                    pass


            elif 'find location' in self.query:
                speak("what is the location")
                location = self.take_command()
                url = "https://google.nl/maps/place/" + location + '/&amp;'
                webbrowser.open(url)
                speak('here is the location' + location)

            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                speak('sir please enter username')
                name = input('enter user name:-')
                webbrowser.open(f'www.instagram.com/{name}')
                speak(f'sir hear is the profile of the user {name}')
                time.sleep(5)
                speak('sir would you like to download  profile pic of this account?')
                condition = self.take_command()
                if 'yes' in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak('i am done sir...')
                else:
                    pass

            elif 'read pdf' in self.query:
                pdf_reader()

            elif 'play a  song' in self.query:
                speak("sir can you please say the name of the song")
                song = self.take_command()
                if 'play' in self.query:
                    song = song.replace('song','')
                    speak("playing" + song)
                    print(f'playing{song}')
                    pywhatkit.playonyt(song)
                    print('playing')
                elif 'download' in self.query:
                    speak("please enter the youtube video link you want to download")
                    link = input('Enter youtube video link:-')
                    yt = YouTube(link)
                    yt.streams.get_highest_resolution().download()
                    speak(f"sir downloaded {yt.title} from the link you given into the main folder")
                elif 'youtube' in self.query:
                    speak("opening youtube")
                    webbrowser.open("https://www.youtube.com/")
                else:
                    speak("no result found")

            elif 'battery' in self.query or 'how much power we have' in self.query:
                battrey = psutil.sensors_battery()  # sensor_battery is a function that show us our battery condition
                percentage = battrey.percent
                speak(f'sir our system have {percentage} percent battery')
                if percentage >= 75:
                    speak('we have enough power to continue our work')
                elif percentage >= 40 and percentage <= 75:
                    speak('we should connect our system to charging point to charge our battery')
                elif percentage <= 15 and percentage <= 30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage < 15:
                    speak("we have very low power, please connect to charging...")

            elif 'internet speed' in self.query:
                speak("wait a few seconds sir, checking your internet speed ")
                st = speedtest.Speedtest()
                dwl = st.download()
                dwl = dwl / 1000000  # converting bytes to megabytes
                upl = st.upload()
                upl = upl / 1000000
                print(f"sir we have {dwl} megabytes per second downloading speed and {upl} megabytes per second uploading "
                    f"speed")
                speak(f"sir we have {dwl} megabytes per second downloading speed and {upl} megabytes per second uploading "
                    f"speed")

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
                speak("volume increased")

            elif 'volume down' in self.query:
                pyautogui.press("volumedown")
                speak("volume decreased")

            elif 'volume mute' in self.query or 'mute' in self.query:
                pyautogui.press("volumemute")
                speak("muted")

            elif 'do some calculations' in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak('sir what you want to calculate')
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,  # addition
                        '-': operator.sub,
                        '*': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak('your result is:')
                speak(eval_binary_expr(*(my_string.split())))

            elif 'take screenshot' in self.query:
                speak('sir, tell me the name of this screenshot file')
                name = self.take_command().lower()
                speak('sir hold the screen for few seconds, i am taking the screenshot')
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f'{name}.png')
                speak('i am done sir, the screenshot is saved inn our main folder. now i am ready for new command')
                

            elif 'temperature' in self.query:
                search = 'temperature in surat'
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"current temperature in surat is {temp}")
                speak(f"current {search} is {temp}")


            elif 'open excel' or 'open microsoft excel' or 'open ms excel' in self.query:
                speak('wait few seconds sir i am opening excel')
                pyautogui.hotkey('win','r')
                time.sleep(1)
                pyautogui.write('excel')
                pyautogui.press('enter')
                time.sleep(2)
                speak('sir what would i do now?')
                # condition2 = self.take_command()
                if 'create a new sheet' or 'create a new blank sheet' or 'create a new sheet' in self.query:
                    pyautogui.hotkey('ctrl','n')
                    time.sleep(1)
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    
                    # condition3 = self.take_command()
                elif 'open old sheet' or 'open my recent document' in self.query:
                    speak('sir please tell me your previous excel file name')
                    cmd = self.take_command() 
                    openpyxl.load_workbook(f'{cmd}.xlsx')
                        

            # elif 'play a  song' in self.query:
            #     speak("sir can you please say the name of the song")
            #     song = self.take_command()
            #     if 'play' in self.query:
            #         song = song.replace('song','')
            #         speak("playing" + song)
            #         print(f'playing{song}')
            #         pywhatkit.playonyt(song)
            #         print('playing')
            #     elif 'download' in self.query:
            #         speak("please enter the youtube video link you want to download")
            #         link = input('Enter youtube video link:-')
            #         yt = YouTube(link)
            #         yt.streams.get_highest_resolution().download()
            #         speak(f"sir downloaded {yt.title} from the link you given into the main folder")
            #     elif 'youtube' in self.query:
            #         speak("opening youtube")
            #         webbrowser.open("https://www.youtube.com/")
            #     else:
            #         speak("no result found")

            elif 'hello' in self.query:
                print("hello sir, may i help you something")
                speak("hello sir, may i help you something")

            elif 'how are you' in self.query:
                print('i am fine sir, what about you')
                speak('i am fine sir, what about you')

            elif 'what is your name' in self.query:
                print('my name is david')
                speak('my name is david')

            elif "my name" in self.query:
                print("sir, your name is Manan")
                speak("sir, your name is Manan")

            elif "my college name" in self.query:
                print("your college name is shree ram krishna institute of computer education and applied science")
                speak("your college name is shree ram krishna institute of computer education and applied science")

            elif "what can you do" in self.query:
                print("i talk with you until you want to stop, i can say time, open your social media account, i can send "
                    "emails, i can search for something in google and i can tell jokes")
                speak("i talk with you until you want to stop, i can say time, open your social media account, i can send "
                    "emails, i can search for something in google and i can tell jokes")

            elif 'i am also good' in self.query or 'fine' in self.query:
                print("that's great to hear from you")
                speak("that's great to hear from you")

            elif 'thank you' in self.query:
                print("it's my pleasure sir")
                speak("it's my pleasure sir")

            elif 'not fine' in self.query:
                print("what happened sir... can i tell you a joke to refresh your mood ")
                speak("what happened sir... can i tell you a joke to refresh your mood ")

            elif 'you can sleep now' in self.query or 'no thanks' in self.query:
                print("okay sir i am going to sleep now you can call me anytime. take care sir")
                speak("okay sir i am going to sleep now you can call me anytime. take care sir")
                break

            speak("do you have any other work sir")

        

    # if __name__ == "__main__": 
    #     while True:
    #         permission = take_command(self)
    #         if 'start the system' in permission:
    #             TaskExecution()
    #         elif 'no thanks' in permission:
    #             speak("thanks for using me, have a good day sir")
    #             sys.exit()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_btn.clicked.connect(self.startTask)
        self.ui.exit_btn.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/processing.gif")
        self.ui.jarvisai.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/voice.gif")
        self.ui.voice_gui.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/lines.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/initialize.gif")
        self.ui.gif_int.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        # now = QDate.currentDate()
        label1_time = current_time.toString('hh:mm:ss')
        # lable2_date = now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label1_time)

app = QApplication(sys.argv)
assistance = Main()
assistance.show()
exit(app.exec_())
