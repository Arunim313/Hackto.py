#CREATE A web request, json file
import tkinter as tk
import json  # {"USD_INR":74.924897}..."key", value
import requests   #to get url

def convert():
    ent2.delete(0,tk.END)
    store = int(ent1.get())
    cr = str(currency.get())
    dr = str(currency1.get())
    ax = requests.get("https://free.currconv.com/api/v7/convert?q=" + cr +"_" + dr + "&compact=ultra&apiKey=")
    ak = json.loads(ax.text) 
    yy = float(ak[cr+"_"+dr])
    ent2.insert(0,store*yy )
   

file = open("C:\\Users\\pc\\Desktop\\ashpy\\list.txt", "r")
lines = []
for line in file: 
    lines.append(line.strip())

print(lines)
 
    
    
root=tk.Tk()
root.geometry("500x500")

l1= tk.Label(root, text="Enter value here")
l2= tk.Label(root, text = "Converted value:" )

currency = tk.StringVar()
currency.set("USD")
drop1 = tk.OptionMenu(root, currency, *lines , command = convert)
ent1 = tk.Entry(root)
ent2 = tk.Entry(root)

currency1 = tk.StringVar()
currency1.set("USD")
drop2 = tk.OptionMenu(root, currency1, *lines , command = convert)

drop1.grid(row=1, column = 3)
drop2.grid(row=2, column = 3)
l1.grid(row=1)
l2.grid(row=2)

ent1.grid(row=1, column=1)
ent2.grid(row=2, column=1)

btn= tk.Button(root, text = "CONVERT", bg="purple", fg="white",command=convert)
btn.grid(row=3, columnspan=2)


root.mainloop()

