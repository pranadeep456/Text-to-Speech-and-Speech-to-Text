#First install pyttsx3, speechRecognition, pyaudio
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init() #initilize pyttsx3

#converting text to speach
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

#converting speach to text
def listen_to_speech():
    recognizer = sr.Recognizer() #initilize Recognizer
    with sr.Microphone() as source:
        print("Listening...Speak now: ")
        audio = recognizer.listen(source) # capture the speech and storing in audio variable
        try :
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand the speech!")
        except sr.RequestError:
            print("Could not request result")

def main():
    while True:
        print("\nChoose any option:")
        print("1. text to speak")
        print("2. speech to text")
        print("3. Exit program")

        try:
            option = int(input("Enter your option(1/2/3)"))

            if option == 1:
                text = "Hello Pranadeep, How are you?"
                speak_text(text)
            elif option == 2:
                listen_to_speech()
            elif option == 3:
                print("Exiting program!")
                break
            else:
                print("Invalid option. please enter below option")
        except ValueError:
            print("Caught Value Error: Option should be Integer, Other characters are not allowed!")
        except Exception as ex:
            print(f"Caught Unknown Error: {ex}")

if __name__ == "__main__":
    main()
