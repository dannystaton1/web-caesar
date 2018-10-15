def alphabet_position(letter):
    return ord(letter.lower()) - ord('a')

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    pos = alphabet_position(char)
    new_char = chr(((pos + rot) % 26) + ord('a'))            #needs modulo
    if char.isupper():
        new_char = new_char.upper()
    return new_char

def encrypt(text, rot):
    ciphertext = ''
    for char in text:
        ciphertext += rotate_character(char, rot)
    return ciphertext

def main():
    msg = input('Type a message: ')
    rot = int(input('Rotate by: '))
    print(encrypt(msg, rot))

if __name__ == '__main__':
    main()
