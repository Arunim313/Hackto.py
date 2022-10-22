contacts = []
contact_numbers = []
number = 5

#Taking input 
for i in range(number):
    name = input("Name: ")
    contact_number = int(input("Phone Number: "))
    
    contacts.append(name)
    contact_numbers.append(contact_number)
    
print("\nNAME\t\tContact Number \n")

for i in range(number):
    print("{}\t\t{}".format(contacts[i],contact_numbers[i]))
    
search_contact = input("\nEnter the name you want to search: ")
print("\nSearch Result: ")

#To search the contact
if search_contact in contacts:
    index = contacts.index(search_contact)
    contact_number = contact_numbers[index]
    print("Name: {},Contact Number: {}".format(search_contact,contact_number))
    
else:
    print("Name not found in the contact book!")