from functies import *

# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap') == 3:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog wat extra testen voor getNumberOfCharacters

# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")
print(getNumberOfSentences(getText('easy')))
# schrijf zelf nog een extra testen voor getNumberOfSentences (gebruik test.txt).

# test 3: getNumberOfWords
if getNumberOfWords(getFileContentAsString('Python/Python/chellenges/challenge5/data/difficult.txt')) == 82:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")
print(getNumberOfWords(getText('difficult')))

if getNumberOfWords(getFileContentAsString('Python/Python/chellenges/challenge5/data/easy1.txt')) == 11:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")
print(getNumberOfWords(getText('easy')))
# schrijf zelf nog een extra testen voor getNumberOfWords (gebruik test.txt).
if getNumberOfWords(getFileContentAsString('/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/Python/Python/chellenges/challenge5/data/test.txt')) == 13:
    print('test is geslagd' )
else:
    print('je hebt een vout')
print(getNumberOfWords(getFileContentAsString('/Users/ilya/Documents/GitHub/School/Softwere dev./SD/Leren-programen/Python/Python/chellenges/challenge5/data/test.txt')))