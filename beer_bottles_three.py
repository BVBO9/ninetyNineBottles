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
    x = 0
    # this is to start the user input prompt. it needs to reject non-integer input
    # ---> currently doesn't reject...
    # update 10:14am 2/12/2025 the while loop rejects string input
    # and breaks from the loop if you enter '0' as the number of beers
    while x == False or 99 < x or x < 0:
        try:
            x = int( input( "How many beer bottles would you like today?\n" ))
            if x == 0:  # this if statement is to stay in the loop
                print( "\nZero bottles of beer on the wall.\nZero bottles of beer.\nWe've taken them down and passed them around.\nNow we're drunk and passed out!" )
                # exit()
                # exit()
                # exit() # this statement is here because the wording is different from the other lyrics
                # as of 10:14am on 2/12/2025 the "0" beer bottles input works perfectly
                break
            elif x > 99:
                print( "I'm sorry, you can't have that many today!" )
            elif x < 0:
                print( "You need to have at least 0!" )
        except:
            ValueError
            print( "Please enter a number 0-99" )
    # this is to start a loop to take an integer 0-99 as correct input
#    if x < 0 or x > 99:
#        print() # for spacing
#        print( "Please enter a number between zero and ninety nine.\n" )
        # try:
            # x = int( input( "How many beer bottles would you like today?\n" ))

        # except:
            # ValueError
            # print( "Please enter a number between zero and ninety nine" )
    # this if statement is here because it won't work in the while loop above
    if x > 0 or ( x <= 99 and x > 0 ):
        for x in range( x, -1, -1 ):
            print()
            print( f"{ x } bottles of beer on the wall." )
            print( f"{ x } bottles of beer." )
            print( f"Take one down and pass it around." )
            print( f"{ x } bottles of beer on the wall." )
user_input() # to call the function to life
###############################################################################################
##############################################################################################
#############################################################################################
############################################################################################
###########################################################################################
# This is a test function to convert integers captured by user input to string numberals. for example from "1 to one" or "2 to two"
# How is the parameter you enter into the first function not a Global Variable???  10:20am 2/12/2025
# def convert_int_to_str( Name ):
#     print( Name )
# convert_int_to_str()
#
# to countdown in your for loop
# for x in range( 5, 0, -1 ):
#    print( x )
#  
# 
# 
# nested loop
#   table_size = 5
#   for i in range( 1, table_size + 1 ):
#       for j in range( 1, table_size + 1 ):
#           print(f"i * j:2", end=" " )
#       print()
#
#
#
#
#
#
##
#
#
#
#
#
#
##
#
#
#
#
#
#
#
