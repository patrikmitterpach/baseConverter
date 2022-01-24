# baseConverter.py
# Converts input numbers from decimal base to a base given by a user.

minBase = 2
maxBase = 16

while True:
    try:
        inputBase = int( input(f'Enter base [{minBase}-{maxBase}]: ') )
        if not minBase <= inputBase <= maxBase:
            raise ValueError
        break
    except ValueError:
        print(f'Invalid base, please enter a valid one. [{minBase}-{maxBase}]')

while True:
    try:
        number = int( input(f'Enter a decimal number to convert to base {inputBase}: '))
        if 0 > number:
            raise ValueError
        break
    except ValueError:
        print('Invalid number, please enter a valid one.')
        

# Variables
#  To expand base selection, edit 
#  possibleModulos to include the needed selection.
returnArray = []
possibleModulos = ['0','1','2','3','4','5','6','7','8','9',
                    'A','B','C','D','E','F']

# Loop
#   Basic algorithm to save to modulos of division by the base
#   to a separate array, which is then returned in reverse order.
while number > 0:
    modulo = int(number % inputBase)
    returnArray.append( possibleModulos[modulo] )
    number = (number - modulo) / inputBase
 
# Output   
returnArray.reverse()
returnNumber = ''.join( returnArray )

print(returnNumber)

