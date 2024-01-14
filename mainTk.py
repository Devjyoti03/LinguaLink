from googletrans import Translator
from tkinter import *
from tkinter import messagebox

def translate_function():
 #check if the source and target languages are empty 
 if (len(src_entry.get("1.0","end-1c"))>1):
   src_v = src_entry.get("1.0","end-1c").lower()
   src_v =src_v.replace(" ","")
 else:
   src_v = None
  
 if (len(dest_entry.get("1.0","end-1c"))>1):
   dest_v = dest_entry.get("1.0","end-1c").lower()
   dest_v =dest_v.replace(" ","")
 else:
   dest_v = None

 if (len(text_entry.get("1.0","end-1c"))<=1):
   messagebox.showerror(message="Enter valid text")
 else:
   text_v = text_entry.get("1.0","end-1c") 
   if (not src_v) & (not dest_v):
     translated_text = translator_object.translate(text_v)
   elif (not src_v):
     translated_text = translator_object.translate(text_v,dest=dest_v)
   elif (not dest_v):
     translated_text = translator_object.translate(text_v,src=src_v)
   else:
     translated_text = translator_object.translate(text_v,src=src_v,dest=dest_v)
   messagebox.showinfo(message = "TRANSLATED TEXT: "+ translated_text.text)

def clear():
 dest_entry.delete("1.0","end-1c")
 src_entry.delete("1.0","end-1c")
 text_entry.delete("1.0","end-1c")

window = Tk()
window.geometry("500x300")
window.title("Language Translator")

translator_object = Translator()

title_label = Label(window, text="Language Translator Using Python",font=("Arial", 20)).pack()

text_label = Label(window, text="Text to Translate:").place(x=10,y=50)
text_entry = Text(window, width=40, height=5,font=("Arial",12))
text_entry.place(x=130,y=50)

src_label = Label(window, text="Source Language (empty: auto-detect):").place(x=10,y=150)
src_entry = Text(window, width=20,height=1,font=("Arial",12))
src_entry.place(x=300,y=150)

dest_label = Label(window, text="Target language (empty: english-default):").place(x=10,y=180)
dest_entry = Text(window, width=20,height=1,font=("Arial",12))
dest_entry.place(x=300,y=180)

button1 = Button(window,text='Translate', bg = 'Lightgreen',command=translate_function).place(x=160,y=230)
button2 = Button(window,text='Clear', bg = 'Pink',command=clear).place(x=270,y=230)

window.mainloop()
