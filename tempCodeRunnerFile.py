
                    if abs(user_number - random_number) <= 4:
                        print("Close but not cigar, try a higher number")
                    else:
                        print("Not even close, try a higher number")
    elif 'n' in choice.lower():
        print("Exiting...")
        break
    else:
        print("Invalid input...please try again")