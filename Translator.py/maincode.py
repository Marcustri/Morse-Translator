import tkinter as tk                        # Import TKinter and use tk as a branch of tkinter for GUI
from tkinter import messagebox              # Import message boxes for the warning messages
from ttkbootstrap import Style, ttk         # Set a base style for TK
import time                                 # Import time for blank audio inbetween words
from playsound import playsound             # Import a play sound package

# Morse Code Dictionary
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
                   }

# Reverse Morse Code Dictionary
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}


# Function to show the 'text to morse code' translation screen
def show_text_to_morse():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Text")
    translation_button.config(text="Translate to Morse Code")
    translation_button.config(command=text_to_morse_code)
    sound_button.config(text="Play morse code")                 # all this code is what is in the root of a screen
    sound_button.config(command=morse_audio)
    translation_frame.pack_forget()
    back_button.pack_forget()
    translation_frame.pack()
    sound_button.pack(pady=5)
    slider.pack(anchor="w")
    speed_label.pack(anchor="w", padx=31)
    back_button.pack(pady=5)


# function to show the morse code to the text screen
def show_morse_code_to_text():
    home_frame.pack_forget()
    translation_frame.pack()
    sound_button.pack_forget()          # same applies here to show different things depending on the chosen screen
    slider.pack_forget()
    speed_label.pack_forget()
    translation_label.config(text="Input Morse Code")
    translation_button.config(text="Translate to Text")
    translation_button.config(command=morse_code_to_text)


# Function to show the home screen
def show_home_screen():
    translation_frame.pack_forget()
    home_frame.pack()
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")


# Function to translate text to morse code
def text_to_morse_code():
    text = input_text.get("1.0", "end").strip().upper()
    if not text:
        messagebox.showwarning("Empty Input", "Enter text")
        return
    # Validate if Morse code is entered
    for fri in text:
        if fri in morse_code_dict.values():
            messagebox.showwarning(
                "Invalid Input", "Cannot input Morse code in this option")
            return

    global morse_code   # have to make this global as I have to make reference to it when doing the audio function
    morse_code = ""     # Make this a temporary value to store the translated letter
    for fri in text:    # string that is stored in fri gets put into datadictionary to find intended morse code
        if fri in morse_code_dict:
            morse_code += morse_code_dict[fri] + "  "
        else:
            morse_code += fri
    output_text.delete("1.0", "end")
    output_text.insert("1.0", morse_code)


# Function to translate Morse Code to Text
def morse_code_to_text():
    morse_code = input_text.get("1.0", "end").strip().split(" ")
    if not morse_code:
        messagebox.showwarning("Empty Input", "Enter Morse code")
        return

    # Validate if letters are entered
    for joke in morse_code:
        if joke.isalpha():
            messagebox.showwarning(
                "Invalid Input", "Cannot input letters in this option")
            return

    text = ""
    for joke in morse_code:
        if joke in reverse_morse_code_dict:
            text += reverse_morse_code_dict[joke]
        else:
            text += joke
    output_text.delete("1.0", "end")
    output_text.insert("1.0", text)


# function to clear the input and output fields and show the home screen
def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    show_home_screen()

# morse code audio function
def morse_audio():
 value = str(int(slider.get()))     # make it a whole number and then a string to make it iterable
 match value:                 # value is the value of the slider then incorporate a case where  to play different speeds
     case "1":
        for character in morse_code:
            if character == "-":
                playsound("morse-T-16wpm-800hz.wav") # plays the intended wav file
            if character == ".":
                playsound("morse-E-16wpm-800hz.wav")
            if character == "/":
                time.sleep(0.15)
            else:
                time.sleep(.1)
     case "2":
        for character in morse_code:
            if character == "-":
                playsound("morse-T-23wpm-800hz.wav")
            if character == ".":
                playsound("morse-E-23wpm-800hz.wav")
            if character == "/":
                time.sleep(0.15)
            else:
                time.sleep(.01)
     case "3":
        for character in morse_code:
            if character == "-":
                playsound("morse-T-27wpm-800hz.wav")
            if character == ".":
                playsound("morse-E-27wpm-800hz.wav")
            if character == "/":
                time.sleep(0.15)
            else:
                time.sleep(.005)


# the main window
window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("720x480")
style = Style(theme="flatly")

# home screen
home_frame = ttk.Frame(window, padding="110")
home_frame.pack()

home_label = ttk.Label(home_frame, text="Select Translation Type",
                       font=('tk.DefaultFont', 30))
home_label.pack(pady=10)

# Text -> Morse Code button
text_to_morse_code_btn = ttk.Button(home_frame, text="Text to Morse Code",
                                    command=show_text_to_morse)
text_to_morse_code_btn.pack(pady=5)

# Morse Code -> text button
morse_code_to_text_btn = ttk.Button(home_frame, text="Morse Code to Text",
                                    command=show_morse_code_to_text)
morse_code_to_text_btn.pack(pady=5)

# translation screen
translation_frame = ttk.Frame(window, padding="20")

# label for input text
translation_label = ttk.Label(translation_frame, text="Input Text", font=('tk.DefaultFont', 20))
translation_label.pack(pady=10)

# input text field
input_text = tk.Text(translation_frame, height=5)
input_text.pack()

# label for output text
output_text_label = ttk.Label(translation_frame, text="Output Text", font=('tk.DefaultFont', 20))
output_text_label.pack()

# output text field
output_text = tk.Text(translation_frame, height=5)
output_text.pack()

# translation button
translation_button = ttk.Button(translation_frame, text="Translate", command=None)
translation_button.pack(pady=5)

# sound button to play audios
sound_button = ttk.Button(translation_frame, text="Play")
sound_button.pack(pady=5)

# slider for the speed
slider = ttk.Scale(translation_frame, from_=1, to=3)
slider.pack(anchor="center")

# label for the speed
speed_label = ttk.Label(translation_frame, text="Speed", font=('tk.DefaultFont', 10))
speed_label.pack(anchor="w", padx=31)

# back button to return to home screen
back_button = ttk.Button(translation_frame, text="Back", command=show_home_screen)
back_button.pack(ipady=10)

# to hide translation screen initially
translation_frame.pack_forget()

# to loop the main window, so it doesn't turn off immediately
window.mainloop()
