import pyttsx3
engine = pyttsx3.init()

def tts(word,rate = 125):
	engine = pyttsx3.init()
	
	engine.setProperty('rate',rate)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)

	engine.say(word)
	engine.runAndWait()