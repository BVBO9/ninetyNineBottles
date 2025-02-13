import num2words as n2w
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
#   "Zero bottles of beer on the wall."
#   "Zero bottles of beer."
#   "We've taken them down and passed them around."
#   "Now we're drunk and passed out!"
#   
#   Functions
#   Loops
#   Decisions                   
#   
#################################################################################################
# This is a function to take user input: must enter nunmber 0 - 99, rejects strings, loops
################################################################################################
x = True
def user_input( x ):
    # this is to start the loop
    x = False
    # this is to start the user input prompt. it needs to reject non-integer input
    # x = 0 or x = False is the same thing to a computer
    while x == 0 or 99 < x or x < 0:
        try:
            x = int( input( "How many beer bottles would you like today?\n" ))
            if x == 0:
                print( "\nZero bottles of beer on the wall.\nZero bottles of beer.\nWe've taken them down and passed them around.\nNow we're drunk and passed out!" )
                break
            elif x > 99:
                print( "I'm sorry, you can't have that many today!" )
            elif x < 0:
                print( "You need to have at least 0!" )
        except:
            ValueError
            print( "Please enter a number 0-99" )
    if x > 0 or ( x <= 99 and x > 0 ):
        # stopped the count at 0 because you don't want it to loop the '0' when it should run the 'zero'
        for x in range( x, 0, -1 ):
            print()
            print( f"{ x } bottles of beer on the wall." )
            print( f"{ x } bottles of beer." )
            print( f"Take one down and pass it around." )
            # variable entered to lower the count for next line
            x = x - 1
            print( f"{ x } bottles of beer on the wall." )
            while x == 0:
                print( "\nZero bottles of beer on the wall.\nZero bottles of beer.\nWe've taken them down and passed them around.\nNow we're drunk and passed out!" )
                break
user_input( x ) # to call the function to life
###############################################################################################
##############################################################################################
#############################################################################################
############################################################################################
###########################################################################################
# 
# 
# nested loop
#   table_size = 5
#   for i in range( 1, table_size + 1 ):
#       for j in range( 1, table_size + 1 ):
#           print(f"i * j:2", end=" " )
#       print()
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
##########################################################################################
#########################################################################################
