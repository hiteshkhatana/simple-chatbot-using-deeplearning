import tkinter
from tkinter import *
from run_program import *
from PIL import Image ,  ImageTk


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot(Cheeku): " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.config(bg="lightblue")
base.title("cheeku- The chatbot")
base.geometry("500x500")
base.resizable(width=FALSE, height=FALSE)

load = Image.open("me.jpg")
load = load.resize((280,280),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
#img.place(x=0, y=0)


ChatLog = Text(base, bd=0, bg="white", height="100", width="50", font="Arial",)
ChatLog.image_create(END, image = render)
ChatLog.insert(END , "\n\n Hi, I'm chiku -( The chatbot ) and I chat alot \n\n")


ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="red", activebackground="green",fg='#ffffff',
                    command= send )


EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")



scrollbar.place(x=470,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=450)
EntryBox.place(x=128, y=401, height=70, width=330)
SendButton.place(x=6, y=401, height=70)
base.mainloop()
