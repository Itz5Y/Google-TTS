from gtts import gTTS

print('Please input text')
text = input('>')
tts = gTTS(text)
tts.save('output.mp3')