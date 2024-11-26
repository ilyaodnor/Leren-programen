EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. Ik kan veel dingen maken met programmeren. Ik kan een website maken. Ik kan een spel maken. Ik kan een chatbot maken. Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
ALLOWED_IN_WORD = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

EASY_TEXT1 = "This is an easy text example."
DIFFICULT_TEXT1 = "This is a more complicated example of difficult text. It has many more sentences!"

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    elif choice == 'easy string':
        return EASY_TEXT1

def getNumberOfCharacters(text: str) -> int:
    count = 0
    for char in text:
        if char in ALLOWED_IN_WORD:
            count += 1
    return count

def getNumberOfSentences(text: str) -> int:
    count = 0
    for char in text:
        if char in ['.', '!', '?']:
            count += 1
    return count

def getNumberOfWords(text: str) -> int:
    words = text.split()
    return len(words)  

print(getNumberOfCharacters(getText('difficult'))) 
print(getNumberOfSentences(getText('difficult')))  
print(getNumberOfWords(getText('difficult')))


def get_avi(text):
    num_sentences = getNumberOfSentences(text)
    num_words = getNumberOfWords(text)

    if num_sentences == 0:
        return 0


    average_words_per_sentence = num_words/num_sentences
    if average_words_per_sentence <= 7:
        return 5
    elif average_words_per_sentence <= 8:
        return 6
    elif average_words_per_sentence <= 9:
        return 7
    elif average_words_per_sentence <= 10:
        return 8
    elif average_words_per_sentence <= 11:
        return 9
    elif average_words_per_sentence <= 12:
        return 10
    else:
        return 11