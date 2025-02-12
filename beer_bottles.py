##################################################################################################
#    
#   ninety nine bottles of beer
#   
#   "Ninety nine bottles of beer on the wall."
#   "Ninety nine bottles of beer."
#   "Take one down and pass it around."
#   "Ninety eight bottles of beer on the wall."
#
#
#	"Zero bottles of beer on the wall."
#	"Zero bottles of beer."
#	"We've taken them down and passed them around."
#	"Now we're drunk and passed out!"
#
#   Functions
#   Loops
#   Decisions                   
#   
#################################################################################################
# This is a function to take user input: must enter nunmber 0 - 99, rejects strings, loops
################################################################################################
def user_input():
    # this is to start the loop
    x = False
    # this is to start the user input prompt. it needs to reject non-integer input  ---> currently doesn't reject
    while x == False: 
        try:
            x = int( input( "How many beer bottles would you like today?\n" ))
        except:
            ValueError
            print( "Please enter a number between 0-99" )
        finally:
    # this is to start a loop to take an integer 0-99 as correct input
            while x < 0 or x > 99:
                print() # for spacing
                print( "Please enter a number between zero and ninety nine.\n" )
                try:
                    x = int( input( "How many beer bottles would you like today?\n" ))
                    if x == 0:  # this if statement is to stay in the loop
                        print( "\nZero bottles of beer on the wall.\nZero bottles of beer.\nWe've taken them down and passed them around.\nNow we're drunk and passed out!" )
                        exit()
                        exit()
                        exit() # this statement is here because the wording is different from the other lyrics
                except:
                    ValueError
                    print( "Please enter a number between zero and ninety nine" )
    # this if statement is here because it won't work in the while loop above
                    if x > 0 or x <= 99:
                        for x in range( x ):
                            print()
                            print( f"{ x } bottles of beer on the wall." )
                            print( f"{ x } bottles of beer." )
                            print( f"Take one down and pass it around." )
            # the following print statements are for testing purposes
            # print(x)
            # x = x - 1
            # print(x)
            # testing the functionality of printing current 'x' value and 'x-1' value
            print( f"{ x } bottles of beer on the wall." )
user_input() # to call the function to life
###############################################################################################
##############################################################################################
#############################################################################################
############################################################################################
###########################################################################################