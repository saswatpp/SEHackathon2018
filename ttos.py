def text_to_speech(string):
    from gtts import gTTS 
    my_tts = string 
    tts = gTTS(text=my_tts, lang='en') 
    tts.save("temp.mp3")
    from pygame import mixer # Load the required library 
    mixer.init() 
    mixer.music.load('temp.mp3') 
    mixer.music.play()
