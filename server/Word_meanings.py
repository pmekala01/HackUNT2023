from PyDictionary import PyDictionary
from gtts import gTTS

def word_meaning(word, Language = 'en'):
    dictionary1 = PyDictionary()

    # Finding Synonym using Dictionary1
    word_meaning = dictionary1.meaning(word)

    # myobj = gTTS(text = word, lang = Language, slow=False)
    # myobj.save("pronounciation.mp3")
    try:
        values = list(*word_meaning.values())
        return values[0].capitalize()
    except:
        return "No meaning found"
        

# print(word_meaning("Happy"))