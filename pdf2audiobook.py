import pyttsx3
import PyPDF2
speaker=pyttsx3.init()
inbook=input("Enter Book Name :")
book=open(inbook,'rb')
pdfReader=PyPDF2.PdfFileReader(book)
startpg=int(input("Enter the Page Number from which you have to start :"))
endpg=int(input("Enter the Page Number from which you have to end :"))
for i in range(startpg,endpg-1):
        page=pdfReader.getPage(i)
        text=page.extractText()
        speaker.say(text)
        speaker.runAndWait()
