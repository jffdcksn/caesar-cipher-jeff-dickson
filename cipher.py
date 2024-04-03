text = input("Please enter a sentence: ")
shift = 5

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char not in alphabet:
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('Please enter a sentence:', message)
    print('The encrypted sentence is:', encrypted_text)

caesar(text, shift)
