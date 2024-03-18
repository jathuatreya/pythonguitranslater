# Clipboard Translator

## Introduction

The Clipboard Translator is a Python script that automatically translates text copied to the clipboard into the desired language using the Google Translate API. It provides a convenient way to quickly translate text without the need to manually input the text into a translation tool.

## Features

- Automatically detects copied text from the clipboard and translates it.
- Supports translation into multiple languages (default is Tamil).
- Displays the translated text in a popup message box.

## How to Use

1. Run the script.
2. Copy text to the clipboard that you want to translate.
3. The script will automatically detect the copied text and translate it into the specified language.
4. A popup message box will display the translated text.

## Requirements

- Python 3.x
- `pyperclip` library (for accessing the clipboard)
- `googletrans` library (for text translation)
- `tkinter` library (for creating GUI message boxes)

## Code Explanation

1. **`translate_text` function**: This function takes the text to be translated and the destination language code (default is 'ta' for Tamil) as input. It uses the `Translator` class from the `googletrans` library to translate the text and returns the translated text.

2. **`show_popup` function**: This function creates a GUI popup message box using the `messagebox.showinfo` function from the `tkinter` library. It displays the translated text in the message box.

3. **`main` function**: This is the main function of the script. It continuously checks the clipboard for any changes in the copied text using the `pyperclip` library. If there's new text copied to the clipboard, it translates the text using the `translate_text` function and displays the translated text in a popup message box using the `show_popup` function.

4. **`if __name__ == "__main__":` block**: This block ensures that the `main` function is executed when the script is run directly (not imported as a module).

## Author

- **Name:** Jathushan Varnakulasingam
- **Project Purpose:** Foundation IIT project in Python

## License

This project is licensed under the [MIT License](LICENSE).
