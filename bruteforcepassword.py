import string
paswd = input("Insert Password to Crack: \n")
def Brute(paswd):
   print("[+][+] Starting BruteForce...")
   charset = list(string.ascii_letters + string.digits + string.punctuation)
   result = ""
   x = 0
   while x <= len(paswd)-1:
      for char in charset:
         pchar = paswd[x]
         if char == pchar:
           print("[+] Trying...", char)
           print("[+][+] Matched (",char, ")")
           result += char
           print("[+][+] Current:",result)
           x += 1
           break
         else:
           print("[+] Trying...",char)     
   print("[+][+] Matching Done - Password Found:", result)
Brute(paswd) 
#Password MaxLenght is : about 10
#This is an old version, BruteForce#2 is more efficent, but this still be a great work for me, about 15 lines of code to check if a string is equal to another string, char by char.
