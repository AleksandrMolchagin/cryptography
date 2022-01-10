import string

"""
 A function to create encoding and decoding dictionaries based on the shift value

    @param: 
        n - the shift value

    @return: 
        encoding and decoding dictionaries
"""
def create_shift_substitutions(n):
    encoding = {}
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)
    
    for i in range(alphabet_size):
        oldLetter = string.ascii_uppercase[i]
        newLetter = string.ascii_uppercase[(i+n)%alphabet_size]
     
        encoding[oldLetter] = newLetter
        decoding[newLetter] = oldLetter
    
    return encoding, decoding

"""
A function to encode the message using shift substitution

    @param:
        message - the message to be encoded
        substDict - the encoding dictionary

    @return:
        encoded message
"""
def encode(message, substDict):
    cipher = ""
    for letter in message:
        if letter in substDict:
            cipher += substDict[letter]
        else:
            cipher += letter
    return cipher

"""
A function to decode the message using shift substitution

    @param:
        message - the message to be encoded
        decodeDict - the decoding dictionary

    @return:
        decoded message
"""
def decode (message, decodeDict):
    return encode(message, decodeDict)

"""
A function to print the mapping alphabet made by the shift substitution

    @param: 
        subst - the substitution dictionary
"""
def printable_substitution(subst):
    mapping = sorted(subst.items())
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(letter for _, letter in mapping)
    print("{}\n{}".format(alphabet_line, cipher_line))

if __name__ == "__main__":
    n = 1 
    encoding, decoding = create_shift_substitutions(n)
    while True:
        print("\nWelcome to the Caesar's Shifty Cipher encoder/decoder!")
        print("--------------------------------------------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode a Message.")
        print("\t3. Decode a Message.")
        print("\t4. Change Shift Value.")
        print("\t5. Exit.")
        print("--------------------------------------------------------")
        choice = input(">> ")
        if choice == '1':
            print("\nEncoding Table:")
            printable_substitution(encoding)
            print("\nDecoding Table:")
            printable_substitution(decoding)
            input("\nPress Enter to continue...")
        elif choice == '2':
            message = input("\nEnter the message to encode: ")
            print("\nEncoded Message: {}".format(encode(message.upper(), encoding)))
            input("\nPress Enter to continue...")
        elif choice == '3':
            message = input("\nEnter the message to encode: ")
            print("\nDecoded Message: {}".format(decode(message.upper(), decoding)))
            input("\nPress Enter to continue...")
        elif choice == '4':
            done = False
            while done == False:
                try:
                    new_shift = int(input("\nEnter the new shift value: \n>> "))
                    if new_shift >= 1:
                        encoding, decoding = create_shift_substitutions(new_shift)
                        n = new_shift
                        done = True
                    else:
                        print("\tShift value must be greater than 0.")
                except ValueError:
                    print("Shift {} is not a valid number.".format(new_shift))
        elif choice == '5':
            print("\nHave a good rest of the day!\n")
            break
        else:
            print('Unknown option "{}"'.format(choice))