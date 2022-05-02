from distutils import core
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import requests
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit as kit
import sys
import pyjokes
import pyautogui as pg
from pyautogui import *


print("Kaamna is initializing")

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


class Widget:
    def __init__(self):

        root=Tk()

        root.title('Kaamna')
        root.geometry('1280x720')

        img = ImageTk.PhotoImage(Image.open(r"C:\Users\bholenathravi\Desktop\TTS_MajorProject\face gui.jpg"))
        panel = Label(root, image = img)
        panel.pack(side='right', fill='both',expand = "no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click Start')

        userFrame = LabelFrame(root, text="Access", font=('Black ops one',12, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left1 = Message(userFrame, textvariable=self.userText, bg='black', fg='white')
        left1.config(font=("Century Gothic", 24, 'bold'))
        left1.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="Kaamna", font=('Black ops one',18, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left2 = Message(compFrame, textvariable=self.compText, bg='black', fg='white')
        left2.config(font=("Century Gothic", 24, 'bold'))
        left2.pack(fill='both', expand='yes')

        

        btn = Button(root, text='Start', font=('Black ops one', 15, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Exit', font=('Black Ops One', 15, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')
        
        self.compText.set('Namaste! I am Kaamna.')
        
        root.bind("<Return>",self.clicked)        
        root.mainloop()

    def clicked(self):
        print("Working")
        query=takeCommand()
        self.userText.set('Listening....')
        self.userText.set(query)
        query=query.lower()

        
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

        elif 'introduce yourself' in query:
            speak("Namaste humankind! I am Kaamna, version 1.0. I was created by Navni Dighe. Since, I was born out of Navni's wish, hence the name Kaamna. Also, indeed her wish is my command!")
            print("Namaste humankind! I am Kaamna, version 1.0. I was created by Navni Dighe. Since, I was born out of Navni's wish, hence the name Kaamna. Also, indeed her wish is my command!")
        
        elif 'What are your functionalities' in query or "what can you do" in query:
             speak("I can open several websites, read the news, tell you the right way to do something and also make your day by telling you a joke!")
             print("I can open several websites, read the news, tell you the right way to do something and also make your day by telling you a joke!")
       
        elif "what else can you do" in query: 
             speak("I can search wikipedia, convert a given text to handwriting, send an email and many more things!")
             print("I can search wikipedia, convert a given text to handwriting, send an email and many more things!")

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'volume up' in query:
            pg.press("volumeup")

        elif 'volume down' in query:
            pg.press("volumedown")

        elif 'mute' in query or 'mute volume' in query:
            pg.press("volumemute")


        elif 'open youtube' in query:
            speak("opening youtube")  
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open facebook' in query.lower():
            speak("opening facebook")  
            url = "facebook.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)  

        elif 'open instagram' in query.lower():
            speak("opening instagram")  
            url = "instagram.com" 
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open gmail' in query.lower():
            speak("opening g-mail")  
            url = "gmail.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")  
            url = "stackoverflow.com" 
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            
        elif 'open pinterest' in query:
            speak("opening pinterest")  
            url = "pinterest.com" 
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

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

        elif 'convert text to handwriting' in query:
            speak("Please input the text sir")
            txt = input("Enter your text here: ")
            try:
                kit.text_to_handwriting(f"{txt}", rgb=(0, 0, 255))
                speak("Ma'am, the converted picture is saved in the same folder")
            except Exception as exe:
                print(exe)
                speak("Sorry Ma'am, I was not able to convert that text")

        elif 'take a screenshot' in query:
            mySS = pg.screenshot()
            mySS.save("ss.png")
        
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'bad joke' in query:
            speak("Sorry to hear that Ma'am. I will try another one.")
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
            kit.sendwhatmsg_instantly(f"+91 {ab}",f"{bc}")
            pg.press("tab")   
            pg.press("enter")
                
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

        elif 'news' in query:
            news()
                 
        elif "are you listening" in query or 'are you still listening' in query:
            speak("Yes Ma'am")

        elif 'thanks' in query or 'thank you' in query:
            speak("You are welcome!")
            print("You are welcome!")

        elif 'do you have something to say' in query:
            speak("Yes, I am glad you witnessed my demo!")
            print("Yes, I am glad you witnessed my demo!")

        elif 'exit' in query:
            exit(False)    


if __name__=='__main__':
    speak('Kaamna is initializing')
    wishMe()
    widget=Widget()
        