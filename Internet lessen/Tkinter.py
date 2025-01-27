from tkinter import *
from speedtest import Speedtest
def test():
    download =  Speedtest().download()
    upload = Speedtest().download()
    download_speed = round(download/(10**6),2)
    upload_speed = round(upload/(10**6),2)
    download_label.config(text='Скорость загрузки: \n' + str(download_speed) + 'MbPs')
    upload_label.config(text='Скорость выгрузки: \n' + str(upload_speed) + 'MbPs')
    return download, upload


root = Tk()
root.title(f'Internet speed')
root.geometry('400x300')
button = Button(root, text = 'Нажми на кнопку: ', font = 40, command= test)
button.pack(side='bottom', pady=20)
download_label = Label(root, text= 'Скорость загрузки: \n', font=20)
download_label.pack(pady = (10,0) )

upload_label = Label(root, text= 'Скорость выгрузки: \n', font=20)
upload_label.pack(pady = (10,0) )
root.mainloop()