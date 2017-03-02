# WJEC Controlled Asessment
# Luck Name Numbers 2016
# Python 3.3.2/3.5.2
import time
def adder(a): #Defines function adder
    while len(str(a)) != 1: #Loops while the size of the string of the number a isn't 1
        b = 0
        for x in str(a): b += int ( x ) #Adds every current "a" value.
        a = int(b) #Sets the value of b as a.
    return a
#List for letters, values, meanings (will be used later)
letters = [" ","-","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
value =   [0,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]
meaning = ["Natural leadders","Natural peacemakers","Creative and optimistic","Hard worker","Value freedom","Carers and providers","Thinkers","Have diplomatic skills","Selfless and generous"]
#Welcome Message  
print(" o----------------------------------------------------------------o\n")
print(" | :: | Lucky Name number calcualtor          v1.0.1 (28/02/2017) |\n")
print(" o----------------------------------------------------------------o\n")
# Assigns the first name to a varible
firstName = input("Please enter your, first name: ").lower()
# Assigns the sure name to a varible 
surName = input("Please enter your, surname: ").lower()
##print("Is your name" ,firstName ,surName," If so wait six seconds if not retun the code")
## time.sleep( 6 ) #What's the point of this?
# Values for first name and surname will be used to find the person lucky name numbers
totalFirstname = 0
totalSurname = 0
totalName = 0
nameMeaning = 0
# Changes letters to corresponding value in firstname
for letter in firstName: totalFirstname += (value [letters.index(letter)])
# Changes letters to corresponding value in surname
for letter in surName: totalSurname += (value [letters.index(letter)])
# Prints total first name value
print("The value of your Firstname is: ", totalFirstname)
# Prints total sur name value
print("The value of your Surname is: ", totalSurname)
# Adds up total firstname and total surname together
totalName = int(totalFirstname) + int(totalSurname)
totalName = adder(totalName)
print("The value for your full name is", totalName)
#Prints lucky name meaning.
nameMeaning = int(totalName) - 1
print ("Your lucky name meaning is: ", meaning[nameMeaning])
