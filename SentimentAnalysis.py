from nltk.sentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
from tkinter import Tk     # from tkinter import Tk for Python 3.x
import PyPDF2
import pyttsx3
from tkinter.filedialog import askopenfilename

def read_pdf_file():
    '''

    This function reads a pdf file to the user.

    '''
    Tk().withdraw()

    filename = askopenfilename()
    print(filename)
    sia = SentimentIntensityAnalyzer()

    def say_something():
        if dict.get('pos') > dict.get('neg') and dict.get('pos') > dict.get('neu'):
            engine = pyttsx3.init(driverName="sapi5")
            voices = engine.getProperty('voices')
            volume = engine.getProperty('volume')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty("rate", 170)  # changing the rate of the voice
            engine.setProperty('volume', volume-0.001)
            print("positive")
            engine.say(dor1)
            engine.runAndWait()
        elif dict.get('neu') > dict.get('neg') and dict.get('neu') > dict.get('pos'):
            engine = pyttsx3.init(driverName="sapi5")
            voices = engine.getProperty('voices')
            volume = engine.getProperty('volume')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty("rate", 160)  # changing the rate of the voice
            engine.setProperty('volume', volume-0.001)
            print("neutral")
            engine.say(dor3)
            engine.runAndWait()
        else:
            engine = pyttsx3.init(driverName="sapi5")
            voices = engine.getProperty('voices')
            volume = engine.getProperty('volume')
            engine.setProperty('voice', voices[1].id)  # changing the voice
            engine.setProperty("rate", 150)  # changing the rate of the voice
            engine.setProperty('volume', volume-0.001)
            engine.say(
                dor2)
            engine.runAndWait()

    pdf_file = open(filename, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
    # Find the number of pages in the PDF document
    number_of_pages = read_pdf.getNumPages()
    print(number_of_pages)
    # Read from page 20 to the end of the PDF document
    for i in range(2, 4):
        # Read the PDF page
        page = read_pdf.getPage(i)
        # Extract the text of the PDF page
        page_content = page.extractText()
        dict = sia.polarity_scores(page_content)
        dor1 = '<pitch absmiddle="10">'+page_content+'</pitch>'
        dor2 = '<pitch absmiddle="6">'+page_content+'</pitch>'
        dor3 = '<pitch absmiddle="5">'+page_content+'</pitch>'
        print(dict)
        say_something()


read_pdf_file()

































# Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# # show an "Open" dialog box and return the path to the selected file
# filename = askopenfilename()
# print(filename)
# sia = SentimentIntensityAnalyzer()


# def say_something():
#     if dict.get('pos') > dict.get('neg') and dict.get('pos') > dict.get('neu'):
#         engine = pyttsx3.init(driverName="sapi5")
#         voices = engine.getProperty('voices')
#         volume = engine.getProperty('volume')
#         engine.setProperty('voice', voices[1].id)
#         engine.setProperty("rate", 170)  # changing the rate of the voice
#         engine.setProperty('volume', volume-0.001)
#         print("positive")
#         engine.say(dor1)
#         engine.runAndWait()
#     elif dict.get('neu') > dict.get('neg') and dict.get('neu') > dict.get('pos'):
#         engine = pyttsx3.init(driverName="sapi5")
#         voices = engine.getProperty('voices')
#         volume = engine.getProperty('volume')
#         engine.setProperty('voice', voices[1].id)
#         engine.setProperty("rate", 160)  # changing the rate of the voice
#         engine.setProperty('volume', volume-0.001)
#         print("neutral")
#         engine.say(dor3)
#         engine.runAndWait()
#     else:
#         engine = pyttsx3.init(driverName="sapi5")
#         voices = engine.getProperty('voices')
#         volume = engine.getProperty('volume')
#         engine.setProperty('voice', voices[1].id)  # changing the voice
#         engine.setProperty("rate", 150)  # changing the rate of the voice
#         engine.setProperty('volume', volume-0.001)
#         engine.say(
#             dor2)
#         engine.runAndWait()


# pdf_file = open(filename, 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
# # Find the number of pages in the PDF document
# number_of_pages = read_pdf.getNumPages()
# print(number_of_pages)
# # init function to get an engine instance for the speech synthesis
# engine = pyttsx3.init()
# # Read from page 3 to the end of the PDF document
# for i in range(20, number_of_pages):
#     # Read the PDF page
#     page = read_pdf.getPage(i)
#     # Extract the text of the PDF page
#     page_content = page.extractText()
#     dict = sia.polarity_scores(page_content)
#     dor1 = '<pitch absmiddle="10">'+page_content+'</pitch>'
#     dor2 = '<pitch absmiddle="4">'+page_content+'</pitch>'
#     dor3 = '<pitch absmiddle="6">'+page_content+'</pitch>'
#     print(dict)
#     say_something()