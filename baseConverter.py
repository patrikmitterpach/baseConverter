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
return_array = []
possible_modulos = ['0','1','2','3','4','5','6','7','8','9',
                    'A','B','C','D','E','F']

# Loop:
while number > 0:
    modulo = int(number%inputBase)
    return_array.append(possible_modulos[modulo])
    number = (number-modulo) / inputBase
 
# Output   
return_array.reverse()
return_number = ''.join(map(str,return_array))

print(return_number)

