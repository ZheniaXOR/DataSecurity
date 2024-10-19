import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message =   "Iye mkx pyyv kvv yp dro zoyzvo cywo yp dro dswo, kxn cywo yp dro zoyzvo kvv yp dro dswo, led iye mkx'd pyyv kvv yp dro zoyzvo kvv yp dro dswo."
rezz =      "I rubbed shoulders with people who spoke of friendship, but who did not have the same values as me at all. Those who make you laugh when everything is going well, but who will never be there when misfortune drowns you. - Nekfeu"
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
SymbolFreq = {
'a' : 0.0808,
'b' : 0.0167,
'c' : 0.0318,
'd' : 0.04,
'e' : 0.1256,
'f' : 0.0217,
'g' : 0.018,
'h' : 0.0527,
'i' : 0.0724,
'j' : 0.0014,
'k' : 0.0063,
'l' : 0.0404,
'm' : 0.026,
'n' : 0.0738,
'o' : 0.0747,
'p' : 0.0191,
'q' : 0.0009,
'r' : 0.0642,
's' : 0.0659,
't' : 0.0915,
'u' : 0.0279,
'v' : 0.01,
'w' : 0.0189,
'x' : 0.0021,
'y' : 0.0165,
'z' : 0.0007,
}

def GetMSE(arr1, arr2):
    mse = 0
    for i in range(len(arr1)):
        mse += (arr1[i]-arr2[i])**2
    return mse/len(arr1)

def GetShift(SymbolTable):
    global SymbolFreq
    FreqReal = list(SymbolFreq.values())
    FreqGiven = list(SymbolTable.values())
    MinMSE = 1000
    MinIndex = 0
    for shift in range(0, 26):
        ShiftedFreq = FreqGiven[shift:] + FreqGiven[:shift]
        val = GetMSE(ShiftedFreq, FreqReal)
        if val < MinMSE:
            MinMSE = val
            MinIndex = shift
    return MinIndex

#Ініціалізація допоміжних змінних
offset_lc = ord('a')
offset_up = ord('A')
alphabet_len = ord('z') - ord('a') + 1
message_lc = message.lower()
letter_map = {}
letter_percentage = {}
decryptedSymbols = {}  #результат
symbolCounter = 0

for i in SymbolFreq.keys():
    letter_map[i] = 0

#Код що відповідає за частотний аналіз закодованого тексту
for symbol in message_lc:
    if ord(symbol) >= offset_lc and ord(symbol) < offset_lc + alphabet_len:
        symbolCounter += 1
        letter_map[symbol] += 1
for key, value in letter_map.items():
    letter_percentage[key] = value/symbolCounter

#Знаходимо величину зсвуву алфавіту для декодування
TrueShift = GetShift(letter_percentage)

#Відновлення зашифрованого тексту
outputMessage = ''
offset = TrueShift
if TrueShift<0:
    TrueShift = alphabet_len + TrueShift
for symbol in message:
    if ord(symbol) >= offset_lc and ord(symbol) < offset_lc + alphabet_len:
        if ord(symbol) - offset_lc - TrueShift < 0:
            symbol = chr(ord(symbol)+alphabet_len- TrueShift)
        else:
            symbol = chr(ord(symbol) - TrueShift)
    elif ord(symbol) >= offset_up and ord(symbol) < offset_up + alphabet_len:
        if ord(symbol) - offset_up - TrueShift < 0:
            symbol = chr(ord(symbol)+alphabet_len - TrueShift)
        else:
            symbol = chr(ord(symbol) - TrueShift)
    outputMessage += symbol
print(outputMessage)