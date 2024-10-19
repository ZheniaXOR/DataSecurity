EncryptedByAlice = "391813c092a2d5ac9acb705dfe41be3df08de67d1145cbcc3f"
EncryptedByAliceBob = "03adeae2c8c2f2336c8a8d312733c2456e76e0b2d9068adc3f"
EncryptedByBob = "72d0954e354045f09461dc4c911d0b58ff8963efb12c34303f"


#INPUT - encoded and decoded hex string
#OUTPUT - list of byte numbers
def GetKey(InputStr, EncodedStr):
    SymbolDecoder = 0
    Key = []
    for i in range(0, len(InputStr), 2):
        FirstSymbol = int('0x' + InputStr[i:i+2], 16)
        FirstSymbolEncoded = int('0x' + EncodedStr[i:i+2], 16)
        for j in range(0, 256):
            if FirstSymbol^j == FirstSymbolEncoded:
                SymbolDecoder = j
                break
        Key.append(SymbolDecoder)
    return Key

def GetDecoded(InputEncoded, Key):
    rez = ''
    for symbol in range(0, len(InputEncoded), 2):
        rez += chr(int('0x' + InputEncoded[symbol:symbol + 2], 16) ^ Key[int(symbol/2)])
    return rez

# Отримуємо ключ шифрування від Боба методом брут форсу
keyBob = GetKey(EncryptedByAlice, EncryptedByAliceBob)

# Розшифровуємо повідомлення, коли воно на останньому етапі передачі (коли зашифровано тільки Бобом)
print(GetDecoded(EncryptedByBob, keyBob))

