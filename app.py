import RPi.GPIO as GPIO
import tkinter as tk

from MorseTranslator import encrypt
from MorseBlink import morseBlink

LED_PIN = 11
MORSE_TIMING = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1) 
        self.grid_columnconfigure(1, weight = 1)

        # widget can take all window
        self.pack(fill=tk.BOTH, expand=1, anchor=tk.CENTER)

        self.message_var = tk.StringVar()
        self.message_var.trace('w', self.limitMessageSize)

        self.textInput = tk.Entry(self, width=12, textvariable=self.message_var)
        # create submit button, link it to submit_callback()
        submitButton = tk.Button(self, text="Submit", command=self.submit_callback)
        # create exit button, link it to exit_callback()
        exitButton = tk.Button(self, text="Exit", command=self.exit_callback)

        # place button at (0,0)
        self.textInput.grid(row=0,columnspan=2)
        submitButton.grid(row=1, column=0)
        exitButton.grid(row=1, column=1)

    def submit_callback(self):
        # Get text from input box
        message = self.message_var.get()
        # Translate word into morse code
        morseCode = encrypt(message)
        print(f"Original Message: {message}")
        print(f"Translated to: {morseCode}")
        # Call the morseBlink function to blink the LED
        morseBlink(morseCode, MORSE_TIMING, LED_PIN)

    def exit_callback(self):
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
        exit()
    
    def limitMessageSize(self, *args):
        value = self.message_var.get()
        if len(value) > 12:
            self.message_var.set(value[:12])
        
root = tk.Tk()
app = Window(root)
root.wm_title("Task 5.3D: Blink Morse code using GUI")
root.geometry("320x320")
root.mainloop()