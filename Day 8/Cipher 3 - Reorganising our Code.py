alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(direction, text, shift):
    cipher = []

    if direction == "encode":
        for letter in text:
            i = alphabet.index(letter)
            j = i + shift
            cipher.append(alphabet[j])
    else:
        for letter in text:
            i = alphabet.index(letter)
            j = i - shift

            if j > 0:
                cipher.append(alphabet[j])
            else:
                j = j * 2 + shift
                cipher.append(alphabet[j])

    print(f"The decoded text is {''.join(cipher)}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction = direction, text = text, shift = shift)