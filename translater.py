import pyperclip
from googletrans import Translator
import tkinter as tk
from tkinter import messagebox

def translate_text(text, dest_lang='ta'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def show_popup(text):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Translated Text", text)

def main():
    last_copied_text = ''
    while True:
        copied_text = pyperclip.paste()
        if copied_text != last_copied_text:
            translated_text = translate_text(copied_text)
            show_popup(translated_text)
            last_copied_text = copied_text

if __name__ == "__main__":
    main()
