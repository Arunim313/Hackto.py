import pyshorteners
url=input("Enter LONG URL : ").strip()
s=pyshorteners.Shortener()
print(s.tinyurl.short(url))
