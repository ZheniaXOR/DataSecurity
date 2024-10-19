#operation= 'ENCODE'
operation= 'DECODE'
n = 5

rotors = ['BDFHJLCPRTXVZNYEIWGAKMUSQO', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ']
message = 'XPCXAUPHYQALKJMGKRWPGYHFTKRFFFNOUTZCABUAEHQLGXREZ'

offset = ord('A')
alphabetLen =len(rotors[0])

if operation == 'ENCODE':
    encoded = ''

    #блок коду що відповідає за алфавітний зсув
    for index, symbol in enumerate(message):
        alphabetNum = n+index
        alphabetNum = alphabetNum % alphabetLen + ord(symbol)
        if alphabetNum>ord('Z'):
           alphabetNum = offset + (alphabetNum - ord('Z') - 1)
        encoded += chr(alphabetNum)
    #print(encoded)

    # блок коду що відповідає за кодуванн через ротори енігми
    for rotor in rotors:
        msg = ''
        for index, symbol in enumerate(encoded):
            alphabetNum = ord(symbol) - offset
            #print(alphabetNum+index+n)
            msg += rotor[alphabetNum]
        encoded = msg
    print(encoded)
else:

    # блок коду що відповідає за зворотній прохід через ротори
    rotors.reverse()
    for rotor in rotors:
        decoded = ''
        for index, symbol in enumerate(message):
            #alphabetNum = ord(symbol) - offset
            #decoded += rotor[alphabetNum]
            alphabetNum = offset + rotor.index(symbol)
            decoded+=chr(alphabetNum)
        message = decoded

    # блок коду що відповідає за зворотній прохід через алфавітний зсув
    decoded = ''
    for index, symbol in enumerate(message):
        alphabetNum = ord(symbol) - (n + index)%alphabetLen
        #print(ord('Z') - (offset - alphabetNum - 1))
        if alphabetNum<offset:
            alphabetNum = ord('Z') - (offset - alphabetNum - 1)
        decoded +=  chr(alphabetNum)

    print(decoded)