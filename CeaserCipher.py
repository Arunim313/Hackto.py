def c_encryption(plaintext,key):
  encryption_str = ''
  for i in plaintext:
    if i.isupper():
      temp = 65 + ((ord(i) - 65 + key) % 26) 
      encryption_str = encryption_str + chr(temp)                              
    elif i.islower():
      temp = 97 + ((ord(i) - 97 + key) % 26)
      encryption_str = encryption_str + chr(temp)
    else:
      encryption_str = encryption_str + i  

  print("The ciphertext is:",encryption_str)

plaintext = input("Enter the plaintext:")
key = int(input("Enter the key:"))
c_encryption(plaintext,key)
