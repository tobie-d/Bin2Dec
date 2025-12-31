import time 

def convert(num):
    total = 0 #Initialize 'total' (the result) and power (bit position)
    power = 0
        
    if len(str(num)) > 8: #Raise an error if binary number has more than 8 digits
        raise ValueError("Number too long! Please only enter 8 digits.") 
    for ch in str(num): 
        if ch not in '01': #Raise error if any character is not '0' or '1'
            raise ValueError("Invalid input! Please only enter 1s and 0s") 
         
    bistr = str(num) #Converts input to string so it can be reversed
    for c in reversed(bistr): #Loops through the number and processes them from LSB to MSB
        if c == '1':
           total += 2 ** power #If the bit is equal to 1, add 2^power
        elif c == '0':
            pass
        power += 1 #Moves to the next bit
    return(total) #Returns the decimal value.



if __name__ == "__main__": #Checks its being ran as a file 
    print("Welcome to the Bin2Dec interface!")
    print("---------------------------------")
    time.sleep(1)
    num = input("Please enter a binary number: ")   #Get binary input from user as a string
    try: #Attempts to convert and catch errors
        print("Converting...") #Cosmetic
        time.sleep(1)
        print(convert(num)) #Calls convert() and prints result
    except ValueError as e: #If any errors have occurred, print it as e
        print(e)
