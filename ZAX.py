
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def time():
   Time = datetime.datetime.now().strftime("%I:%M:%S")
   speak("Current Time is")
   speak(Time)

def   date():
   year = int(datetime.datetime.now().year)
   month = int(datetime.datetime.now().month)
   day = int(datetime.datetime.now().day)
   speak("The current date is")
   speak(day)
   speak(month)
   speak(year)

def   wishme():
   speak("Welcome  Back Sir")
   time()
   date()
   cpu()
   speak("ZAX at  your  servis  Please  tell  me  how  can  i  help  you")

def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 0.5
      audio = r.listen(source)

   try:
      print("Recongnizning...")
      query = r.recognize_google(audio, language='en-in')
      print(query)
   except Exception as e:
      print(e)
      print("Say that Again please")
      speak("Say that Again please...")
      return "None"
   return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\Study Material\Python\Zax Project\ss.png")

def logout():
    os.system("shutdown /l")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
   joke = pyjokes.get_joke()
   speak(joke)
   print(joke)







if __name__ == "__main__":
   wishme()
   while True:
      query = takeCommand().lower()
      if 'time' in query:
          time()
      elif 'date' in query:
          date()
      elif 'wikipedia' in query:
          speak("searching...")
          query = query.replace("wikipedia","")
          result = wikipedia.summary(query, sentences=2)
          print(result)
          speak(result)
      elif 'search in chrome' in query:
          speak("what should i search?")
          chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
          search = takeCommand().lower()
          wb.get(chromepath).open_new_tab(search+'.com')
      elif 'play song' in query:
          songs_dir = ''
          songs = os.listdir(songs_dir)
          os.startfile(os.path.join(songs_dir), songs[0])
      elif 'remember that' in query:
          speak('what should i remember ? ')
          print("speak...")
          data = takeCommand()
          speak("you said me to remember that"+data)
          remember = open('data.txt', 'a')
          remember.write(data)
          print("done")
          remember.close()
      elif 'do you remember anything' in query:
          remember = open('data.txt', 'r')
          print(remember)
          speak("you said me to remember that"+remember.read())
      elif 'screenchot' in query:
          screenshot()
          speak('owari')
      elif 'cpu' in query:
          cpu()
      elif 'hello' in query:
         speak("hello sir, how can i help you?")
      elif 'joke' in query:
          jokes()
      elif 'logout' in query:
          logout()
      elif 'shutdown' in query:
          os.system("shutdown /s /t 1")
      elif 'restart' in query:
          os.system("shutdown /r /t 1")
      elif 'offline' in query:
          quit()