# Code => 
def normal_pattern(n):
    for i in range(n):
        print(("*")*(i+1))

def reverse_pattern(n):
    for i in range(n):
        print(("*")*(n-i))


rows = int(input("Enter the number of rows you want to print: "))
condition = True
while True:
    num = int(input("Type 0 or 1 : "))
    if(num==1):
        condition=True
        break
    elif(num==0):
        condition=False
        break
    else:
        print("Invalid input")
        continue

if condition==True:
    normal_pattern(rows)
elif condition==False:
    reverse_pattern(rows)
