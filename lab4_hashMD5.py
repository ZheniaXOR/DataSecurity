import hashlib

def crack(hash):
    for i in range(100000): #brute force
        if i < 10000:
            DecPower = len(str(i))
            pin = (5-DecPower) * '0' + str(i)
        else:
            pin = str(i)
        BruteForceHash = hashlib.md5(pin.encode())
        BruteForceHash_str = BruteForceHash.hexdigest()
        if BruteForceHash_str == hash:
            return pin
    return pin

InputHash = '86aa400b65433b608a9db30070ec60cd' #pincode 00078
print(crack(InputHash))