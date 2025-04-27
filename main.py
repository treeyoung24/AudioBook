import pyttsx3 
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# Make a for loop to read all data from all pages

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init() # Initialize the text to speech
    player.say(text)
    player.runAndWait()


