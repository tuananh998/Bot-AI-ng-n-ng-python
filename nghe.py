import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
nghe=pyttsx3.init()
voice=nghe.getProperty('voices')
nghe.setProperty('voice',voice[1].id)
def speak(audio):
    print('Thông tuệ vương.' + audio)
    nghe.say(audio)
    nghe.runAndWait()
speak("Chào Tuấn Anh ")
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Buổi sáng tốt lành thưa ông chủ")
    elif hour >=12 and hour <18:
        speak("Buổi trưa tốt lành thưa ông chủ")
    elif hour >=18 and hour <24:
        speak("Buổi tối tốt lành thưa ông chủ")
    speak('Ông chủ cần giúp gì')
def command():
    c=sr.Recognizer()
    with sr.Microphone() as soure:
        c.pause_threshold=2
        audio=c.listen(soure)
    try:
        query=c.recognize_google(audio,language='vi')
        print("Tuấn Anh :" + query)
    except sr.UnknownValueError:
      print("Bạn muốn tìm gì?")
      query=str(input('Có phải bạn muốn tìm gì không?'))
    return query
    
if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("Tuấn Anh cần tìm gì?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak("Tuấn Anh cần tìm gì?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "time" in query:
            time()
        if "facebook" in query:
            speak("HTuấn Anh cần tìm gì?")
            search=command().lower()
            url=f"https://www.facebook.com/?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on facebook')
        if "facebook" in query:
            speak("Tuấn Anh cần tìm gì?")
            search=command().lower()
            url=f"https://www.facebook.com/?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on facebook')
