import pyttsx3 #talk to speech
import datetime # tell you date and time
import speech_recognition as sr
import wikipedia
import webbrowser
import os

JARVIS = pyttsx3.init('sapi5') # initializing pyttsx3
voices = JARVIS.getProperty('voices')
JARVIS.setProperty('voice',voices[0].id)
voiceRate = 150
JARVIS.setProperty('rate',voiceRate)
def speak(audio): # to speak
    JARVIS.say(audio)
    JARVIS.runAndWait()



def wishMe():
    '''
    it will wish you as per time. to know what time is then  you have to use
    '''
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening sir.")
    
    speak("this is jarvis.how can I help you?")

def takeCommand ():
    # it takes microphone input from the user and return string output.
    '''
    what this funtion will do is that it will try to recongnize what are you saying.
    here we have to import speech recong..
    we also have to download pyaudio
    it will listen what are you saying and then the google translater will translete it and then it will print what are you saying.

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("listening....")
        r.pause_threshold = 1 # doesn't complete your phrase 
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source) # will listen what you r saying
        print("done")
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query # if it recognize then it wil print your query(what you r saying)


if __name__ == "__main__":
    wishMe()
    

    while True:
        query  = takeCommand().lower() # this will convert your command into lower case.
        print(query)
        if 'wikipedia' in query:
            print("inside if")
            speak("searching on wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            speak('any thing else sir?')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('any thing else sir?')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('any thing else sir?')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak('any thing else sir?')  
        
        elif 'open dps pune' in query:
            webbrowser.open("dpspune.com")
            speak('any thing else sir?')

        elif 'open github' in query:
            webbrowser.open("github.com")
            speak('any thing else sir?')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is {strtime} sir.')
            speak('any thing else sir?')

        elif 'open code' in query:
            codePath="C:\\software\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('any thing else sir?')
        
        elif 'open mp3' in query:
            webbrowser('mp3skulls.to')
            speak('any thing else sir?')
        
        elif 'thanks' in query:
            speak('welcome sir')

        elif 'bye' in query:
            speak('bye bye sir.')

        elif 'thanks and bye' in query:
            speak('welcome sir.  bye bye')

        elif 'no' in query:
            speak('ok sir.') 

        elif 'how are you' in query:
            speak('I am good. how about  you?')

        elif 'I am also good' in query:
            speak('glad to hear that sir')

    







 