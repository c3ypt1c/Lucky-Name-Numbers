# WJEC Controlled Asessment
# Luck Name Numbers 2016
# Python 3.3.2/3.5.2
def adder(a): #Defines function adder
    while len(str(a)) != 1: #Loops while the size of the string of the number a isn't 1
        b = 0
        for x in str(a): b += int ( x ) #Adds every current "a" value.
        a = int(b) #Sets the value of b as a.
    return a

#List for letters, values, meanings (will be used later)
#Put into a seperate class for optimisation. (not to be initialised every time the program need so run)
class values: 
    letters = [" ","-","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    value =   [0,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]
    meaning = ["Natural leadders","Natural peacemakers","Creative and optimistic","Hard worker","Value freedom","Carers and providers","Thinkers","Have diplomatic skills","Selfless and generous"]

def totalVal(fullname):
    total = 0;
    #For exery name in full name...
    for name in fullname:
        #and for every letter in each name...
        for letter in str(name):
            #add to the total value...
            total += (values.value [values.letters.index(letter)])
            #Note: values is the class and the "." means 'from' so values.value would mean 'from values get value'
    return total;
#A function accepting "name" as a varable from caller.
def calc(name):
    #If a person has more than just a surname and a first name, split into multiple strings.
    #Adds to the total value.
    total = adder(totalVal(name.lower().split(" ")))
    #prints total value of the full name for debug
    print("The value for your full name is", totalVal(name.lower().split(" ")))
    #Prints lucky name meaning for debug
    print("Your lucky name meaning is: ", values.meaning[total-1])
    return values.meaning[total-1]
