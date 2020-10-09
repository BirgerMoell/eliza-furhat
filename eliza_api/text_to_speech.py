import pyttsx3
test = "Once upon a time, a person was trying to convert text to speech using python"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices: 
 print("Voice:") 
 print(" - ID: %s" % voice.id) 
 print(" - Name: %s" % voice.name) 
 print(" - Languages: %s" % voice.languages) 
 print(" - Gender: %s" % voice.gender) 
 print(" - Age: %s" % voice.age)

en_voice_id = "com.apple.speech.synthesis.voice.Alex"
engine.setProperty('voice', en_voice_id)
engine.say(test)
engine.runAndWait()