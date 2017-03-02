import fun;
from time import sleep;
# Start of the program message
print(" o----------------------------------------------------------------o\n")
print(" | :: | Lucky Name number calcualtor          v1.0.1 (28/02/2017) |\n")
print(" o----------------------------------------------------------------o\n")
print("Press Ctrl+c to quit")
#
while True:
    try:
        # Print new line
        print ( "\n" )
        # Assigns the first name to a varible
        firstName = input("Please enter your, first name: ").lower()
        # Assigns the sure name to a varible 
        surName = input("Please enter your, surname: ").lower()
        # Calculates using the function calc() inside "fun.pyw".
        # Prints total first name value
        print("The value of your Firstname is: ", fun.totalVal(firstName))
        # Prints total sur name value
        print("The value of your Surname is: ", fun.totalVal(surName))
        totalName = fun.calc(str(firstName) + " " + str (surName))
        # Notice how there are no prints yet, you can
        # still get the value and the meaning of the name.
    except KeyboardInterrupt:
        break;
    
print ( "Bye..." );
sleep(5);
