def inputi(*whatsay): #This doesn't need to be there. I just like it here.
    while True:
        try:
            return input ( whatsay[0] )
            break
        except IndexError:
            whatsay = ( "> ", )
        except KeyboardInterrupt:
            print ( "" )
            return None
        except:
            print ( Exception )
 
letters = { "a": 1, #A dictionary.
            "j": 1, #It has a number attatched to a string
            "s": 1, #If "s" will be called, 1 will be returned.
            "b": 2, #You call using varable[letter]
            "k": 2, #For example, on the IDLE shell,
            "t": 2, #>>> a = letters["a"]
            "c": 3, #>>> a
            "l": 3, #1
            "u": 3, #>>> h = letters["h"]
            "d": 4, #>>> a + h
            "m": 4, #9
            "v": 4,
            "e": 5,
            "n": 5,
            "w": 5,
            "f": 6,
            "o": 6,
            "x": 6,
            "g": 7,
            "p": 7,
            "y": 7,
            "h": 8,
            "q": 8,
            "z": 8,
            "i": 9,
            "r": 9 }
 
number = [ None,                                #0 (nothing since 0 doesn't exist)
           "Natural Leaders",                   #1
           "Natural peacemakers",               #2
           "Creative and optimistic",           #3
           "Hard workers",                      #4
           "Value Freedom",                     #5
           "Carers and providers",              #6
           "Thinkers",                          #7
           "Have diplomatic skills",            #8
           "Selfless and generous"              #9
           ]
 
while True:
    sums = 0
    for x in inputi().lower().split(" "):       #Use input("> ") if inputi is not defined.
        for y in x:
            sums += letters[y]
 
    while True:
        array = []
        sums = str ( sums )
        if len ( sums ) == 1:                   #If the number is chosen, the loop will break
            sums = int ( sums )
            break
        for x in sums: array.append( int ( x )) #Adds all numbers into an array 
        sums = 0
        for x in array:
            sums += int ( x )                   #Adds all the numbers from the array together. 
 
    print ( number[sums] )

    
