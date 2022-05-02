from importlib import import_module
import requests
from time import time
import pyttsx3 
from requests.api import head
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import requests
from pywikihow import search_wikihow
from wikipedia.wikipedia import random
from webbrowser import get
from bs4 import BeautifulSoup
import pywhatkit as kit
import sys
import pyjokes
import pyautogui as pg
import socket
import pywhatkit as kit

  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Kaamna. Please tell me how may I help you") 

def takeCommand():
    #It takes microphone input from the user and returns string output.
    

        r = sr.Recognizer()
        with sr.Microphone() as source:
           print("Listening...")
           r.pause_threshold = 1
           audio = r.listen(source)
        
        try:
           print("Recognizing...")    
           query = r.recognize_google(audio, language='en-in')
           print(f"User said: {query}\n")
        
        except Exception as e:
           # print(e)    
           print("Say that again please...")  
           return "None"
        
        return query 

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('kaamna6894@gmail.com','assistantkaamna6894') #Enter your email id and password
        server.sendmail('kaamna6894@gmail.com',to,content) #Enter the email id of sender again
        server.close()

def news():
        res = requests.get('https://www.indiatoday.in/india')
        soup = BeautifulSoup(res.text, 'lxml')

        news_box = soup.find('div', {'class': 'view view-category-wise-content-list view-id-category_wise_content_list view-display-id-section_wise_content_listing view-dom-id- custom'})
        all_news = news_box.find_all('a')
     
        i=1
        for news in all_news:
            results = print(news.text)
            print()
            speak(news.text)
            i = i+1
            if(i > 5):
                break

if __name__ == '__main__':
    wishMe() 
  
    while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'who are you' in query:
                speak("I am Kaamna")
                print("I am Kaamna")

            elif 'open command prompt' in query:
                os.system('start cmd')


            elif 'volume up' in query:
                pg.press("volumeup")

            elif 'volume down' in query:
                pg.press("volumedown")

            elif 'mute' in query or 'mute volume' in query:
                pg.press("volumemute")


            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")   
    
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")

            elif 'open pinterest' in query:
                webbrowser.open("pinterest.com")    

            elif 'music' in query:
                music_dir = 'C:\\Users\\bholenathravi\\Desktop\\Playlist'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%H:%S")
                speak(f"It's {strTime}")

            elif "temperature" in query:

                inp = "indore"
                search = f"temperature in {inp}"
                ur = f"https://google.com/search?q={search}"
                r = requests.get(ur)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"Current {search} is {temp}")
        
            elif 'tell me a joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)
                print(joke)

            elif 'bad joke' in query:
                speak("Sorry to hear that Ma'am. I will try another.")
                jok = pyjokes.get_joke()
                speak(jok)
                print(jok)

            elif "activate how to do mode" in query:
                speak("how to do mode is activated please tell me what you want to know")
                how = takeCommand().lower()
                max_result = 1
                how_to = search_wikihow(how, max_result)
                assert len(how_to)==1
                how_to[0].print()
                speak(how_to[0].summary)

            elif 'send a whatsapp message' in query:
                speak("Whom should I send the message Ma'am?")
                ab = int(input("Please Enter Number: "))
                speak("What message should be sent Ma'am?")
                bc = takeCommand().lower()
                speak("Please Enter the hour in which message is to be sent")
                cd = int(input("Please Enter the hour in which message is to be sent: "))
                speak("Please Enter the minutes please enter 3 minutes more than actual time")
                
                de = int(input("Please Enter the minutes in which message is to be sent: "))
                kit.sendwhatmsg(f"+91 {ab}",f"{bc}", cd,de)
                pg.press("tab")

            elif 'send an email' in query:
                try:
                    speak("Whom should I send the email Ma'am")
                    to = input("Reciever's Email ID: ")
                    speak("What should I say Ma'am?")
                    content = takeCommand().lower()
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Ma'am I was not able to send the email.")


            elif 'open camera' in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cap.destryoAllWindows() 
         
            elif 'search on youtube' in query: 
                speak("Ma'am, What should I search on youtube?")
                cm = takeCommand().lower()
                webbrowser.open("https://youtube.com//search?q="+f"{cm}")

            elif 'search on google' in query: 
                speak("Ma'am, What should I search on google?")
                cm = takeCommand().lower()
                webbrowser.open("https://google.com//search?q="+f"{cm}")

            elif "are you listening" in query or 'are you still listening' in query:
                speak("Yes Ma'am")

            elif "what else can you do" in query or "what can you do" in query:
                speak("I can open google, open youtube, search wikipedia, share news, operate whatsapp, tell jokes and many more things")


            elif 'news' in query:
               news()
                 

            elif 'exit' in query:
                exit(False)    

            