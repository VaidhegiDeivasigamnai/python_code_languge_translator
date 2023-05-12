from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter
import tkinter.ttk
import googletrans
import tkinter.messagebox
import textblob


translate = Tk()
translate.title("Simple Translator")
translate.geometry("830x300")
translate.configure(bg="#9A32CD")

def click():
    
    translated_text.delete(1.0, END)

    try:
       
        #get languages from language key
        for key, value in languages.items():
            if (value == default_language.get()):
                from_language_key = key
                break
        
        for key, value in languages.items():
            if (value == translated_language.get()):
                to_language_key = key
                break

        #converrt to textblob
        text = textblob.TextBlob(actual_text.get(1.0, END))

        #translate command
        text = text.translate(from_lang=from_language_key , to=to_language_key)

        #translate output
        translated_text.insert(1.0, text)

    except Exception as e:
        tkinter.messagebox.showerror("Language error", e)

            #google translate
languages = googletrans.LANGUAGES

language_list = list(languages.values())


#text box
actual_text = Text(translate, height=8, width=32)
actual_text.grid(row=0, column=0)
actual_text.grid(padx=20, pady=20)
actual_text.configure(bg="#FFEBCD")

translate_button = Button(translate, text="Translate",command=click)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(translate, height=8, width=32)
translated_text.grid(row=0, column=2)
translated_text.grid(padx=20, pady=20)
translated_text.configure(bg="#FFEBCD")

#language
default_language = ttk.Combobox(translate, width=50, value=language_list)
default_language.current(21)
default_language.grid(row=1, column=0)

translated_language = ttk.Combobox(translate, width=50, value=language_list)
translated_language.current(26)
translated_language.grid(row=1, column=2)

translate.mainloop()
