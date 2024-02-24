from pytube import YouTube
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_youtube_url():
    speak("Please tell me the YouTube URL you'd like to play during the call.")
    youtube_url = input("Enter the url: ")
    return youtube_url

def download():
    try:
        url = get_youtube_url()
        yt = YouTube(url)
        
        video_stream = yt.streams.filter(file_extension='mp4').first()
        
        if video_stream:
            print("\nDownloading video....")
            video_stream.download()
            speak("\nVideo Downloaded Successfully\n")
        else:
            speak("\nVideo download failed. No suitable stream found.\n")
            
    except Exception as e:
        speak(f"\nError during video download: {e}\n")

if __name__ == "__main__":
    download()
