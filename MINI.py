import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import time
import smtplib
print("*****VIRTUAL MINI******")
print("Here We can ask 1.wikipedia /n2.Open Youtube /n3.open google /n4.open gmail /n4.open firefox"
" /n5.search.... /n6.who are you /n7.who created you /n8.Email to friend")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak (audio):
    engine.say(audio)
    engine.runAndWait() 
def wishMe():
    hour=int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am MINI, please tell me how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing.....")
            query='something'
            query=r.recognize_google(audio,language='en-in')
            print("User said:{query}\n")
        except sr.UnknownValueError :
            print("Attention! Google could not understand audio")
            query='could not understand anything'
        except sr.RequestError as e:
            print(e)
        print(query)         
        return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sanikanavale93@gmail.com','')
    server.sendEmail('me@gmail.com')
    server.quit()
if __name__ == "__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query =query.replace('wikipedia', "")
        results=wikipedia.summary(query,sentences=3)
        speak("According to wikipedia...")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open chrome' in query:
        webbrowser.open("chrome.com")
    elif 'open firefox' in query:
        webbrowser.open('firefox.com')
    elif 'open gmail' in query:
        webbrowser.open('gmail.com')

    elif 'play music' in query:
        music_dir='C:\\Users\\Sanika Navale\\Music\\USB Drive'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'who are you' in query or 'what can you do' in query:
            speak('I am mini your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
    elif 'who created you' in query:
        speak("I am created by group number 25")
        print("I am created by group number 25")

    elif 'search'  in query:
        query = query.replace('search', "")
        webbrowser.open_new_tab(query)
        time.sleep(5)	

    elif 'time' in query:
        str=time.localtime()
        strtime=time.asctime(str)
        speak(strtime)
        
    elif 'open code' in query:
        codepath="C:\\Users\\Sanika Navale\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    
    elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(3)
    elif 'news' in query:
            news = webbrowser.open_new_tab('https://www.hindustantimes.com/india-news?utm_source=google&utm_medium=cpc&utm_campaign=directtraffic_brand_indianews&utm_term=hindustan%20times&utm_campaign=&utm_source=adwords&utm_medium=ppc&hsa_acc=2141919593&hsa_cam=15465643136&hsa_grp=133559430954&hsa_ad=588505569591&hsa_src=g&hsa_tgt=kwd-20280760&hsa_kw=hindustan%20times&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=EAIaIQobChMIqdXK1-zj9gIVEg4rCh3hDgiMEAAYASAAEgIfBPD_BwE')
            speak('Here are some headlines from the hindustan times,Happy reading')
            time.sleep(5)

    elif'email to friend' in query:
        try:
            speak("What should I say?")
            content= takeCommand()
            to="sanikanavale93@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!!")
        except Exception as e:
            print(e)
            speak("Sorry my friend . I am not able to send the mail")



        