import tkinter as tk
import pyttsx3
from PIL import Image,ImageTk



window= tk.Tk()
window.geometry('500x500')
window.title('Inner thoughts')

bedtime=('Music is the ocean\n'
'That pulls me to the shore\n'
'Music is the rhythm\n'
'That moves me to the core\n'
'Music is the therapy\n'
'I need when I feel blue\n'
'Music lifts my spirits\n'
'To make sure I pull through\n'
'The times when I am most cheerful,\n'
'It is clear music was there\n'
'Music is the needed friend\n'
'When no one seems to care\n')


yoo= ImageTk.PhotoImage(Image.open('geetu.jpg'))

def text():
    yoo= pyttsx3.init()
    yoo.say(bedtime)
    yoo.runAndWait()

label= tk.Label(window, text='Poem', font=('Arial, 14'), bg='black', fg='white')
label.pack()

canvas= tk.Canvas(window, width= 600, height= 400, bg="white")
image = canvas.create_image(0, 0, anchor='nw', image=yoo)
canvas.create_text(250,160, text=bedtime,fill='black',font=('Serif', 14))
canvas.pack()

click= tk.Button(window, text='Click',command=text, font=('Arial', 14))
click.pack(side='bottom')
window.mainloop()