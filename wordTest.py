import speech_recognition as sr
from textToSpeech import tts

def speakWordMic(word):
    r = sr.Recognizer()
    mic = sr.Microphone()

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        with mic as source:
            print("Loading...")
            r.adjust_for_ambient_noise(source)
            print("Speak!")
            audio = r.listen(source)
            response["transcription"] = r.recognize_google(audio, language='en-US')

            if response["transcription"].lower() == "help":
                tts(word)
                print("Hope this helps!")
                return False

            guess_is_correct = response["transcription"].lower() == word.lower()

            return guess_is_correct
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavaliable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return False
    

if __name__ == "__main__":
    while True:
        word = input("What word do you want to test on? ")
        if not word.lower() == "help":
            break
        else:
            print("That is not a valid word do to keyword allocation.")

    while True:
        if speakWordMic(word):
            print("Good Job");
            break
        else:
            print("Try again");