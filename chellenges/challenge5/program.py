from functies import *
import tkinter as tk
import tkinter.messagebox # if you want to send messages to the user.

# functions
def calculate():
    textToBeCalculated = calculateInput.get('1.0', 'end') # get all the text from inputfield
    characterLabel.config(text=f"Characters: {getNumberOfCharacters(textToBeCalculated)}")
    sentencesLabel.config(text =f"Zinnen: {getNumberOfSentences(textToBeCalculated)}")
    aviLabel.config(text = f'AVI: {get_avi(textToBeCalculated)}')


#variables TK
root = tk.Tk()              # create tkInter window
root.title('Text analyser') # set title
root.geometry('1920x1080')    # set dimension
calculateInput = tk.Text(root, width = 70, height = 30, background='lightgrey')            # generate imput element
calculateButton = tk.Button(root, text='Bereken score(s)', command=calculate)      
characterLabel = tk.Label(root, text=f'Karakters:', width=20, bg='black', fg='white') 
sentencesLabel = tk.Label(root, text=f'Zinnen:', width=20, bg='black', fg='white')   
aviLabel = tk.Label(root, text=f'AVI:', width=20, bg='black', fg='white')   


calculateInput.place(x=20, y=20) 
calculateButton.place(x=20, y=520)
characterLabel.place(x=180, y=560)
sentencesLabel.place(x=20, y=560)
aviLabel.place(x=360, y=560)  

root.mainloop() 
