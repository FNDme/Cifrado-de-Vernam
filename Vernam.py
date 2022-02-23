import random

def keygen(length):
    random.seed()
    key = ""
    for i in range(length):
        temp = random.randint(0, 1)
        key += str(temp)
    return key

def encrypt(txt, key = None):
    bin_txt = txt_to_bin(txt)
    temp = dict()
    temp['cripted_bin'] = ""
    if key == None:
        temp['key_bin'] = keygen(len(bin_txt))
    else:
        temp['key_bin'] = txt_to_bin(key)
    for i in range(len(bin_txt)):
        if temp['key_bin'][i] == '0':
            temp['cripted_bin'] += bin_txt[i]
        else:
            temp['cripted_bin'] += str(int(bin_txt[i]) ^ 1)
    temp['cripted_ascii'] = bin_to_txt(temp['cripted_bin'])
    temp['key_ascii'] = bin_to_txt(temp['key_bin'])
    return temp
    

def decrypt(cipher):
    cripted_bin = txt_to_bin(cipher['cripted_ascii'])
    key = txt_to_bin(cipher['key_ascii'])
    plain = ""
    for i in range(len(cripted_bin)):
        if key[i] == '0':
            plain += cripted_bin[i]
        else:
            plain += str(int(cripted_bin[i]) ^ 1)
    return bin_to_txt(plain)

def txt_to_bin(txt):
    return ''.join('{0:08b}'.format(ord(x), 'b') for x in txt)

def bin_to_txt(bin):
    return ''.join(chr(int(bin[i:i+8], 2)) for i in range(0, len(bin), 8))


def menu():
    print("""
    1. Encrypt
    2. Decrypt
    3. Exit
    """)
    choice = int(input("Enter your choice: "))
    return choice

def main():
    while True:
        choice = menu()
        if choice == 1:
            txt = input("Enter a text: ")
            needkey = input("Do you have a key? (y/n) ")
            if needkey == 'y' or needkey == 'Y' or needkey == 'yes' or needkey == 'Yes' or needkey == 'YES':
                key = input("Enter the key: ")
                cipher = encrypt(txt, key)
            else:
                cipher = encrypt(txt)
            print("\nEntrada:")
            print("\tMensaje original: \t\t" + txt)
            print("Salida:")
            print("\tMensaje original en binario: \t" + txt_to_bin(txt))
            print("\tLongitud del mensaje binario: \t" + str(len(txt_to_bin(txt))))
            print("Entrada:")
            print("\tClave: \t\t\t\t" + cipher['key_ascii'])
            print("\tClave en binario: \t\t" + cipher['key_bin'])
            print("Salida:")
            print("\tMensaje cifrado en binario: \t" + cipher['cripted_bin'])
            print("\tMensaje cifrado: \t\t" + cipher['cripted_ascii'])
        elif choice == 2:
            cipher["cripted_ascii"] = input("Enter the text to decrypt: ")
            cipher["key_ascii"] = input("Enter the key: ")
            print("\nEntrada:")
            print("\tMensaje cifrado: \t\t" + cipher['cripted_ascii'])
            print("Salida:")
            print("\tMensaje cifrado en binario: \t" + txt_to_bin(cipher['cripted_ascii']))
            print("\tLongitud del mensaje binario: \t" + str(len(txt_to_bin(cipher['cripted_ascii']))))
            print("Entrada:")
            print("\tClave: \t\t\t\t" + cipher['key_ascii'])
            print("\tClave en binario: \t\t" + txt_to_bin(cipher['key_ascii']))
            print("Salida:")
            print("\tMensaje original: \t" + decrypt(cipher))
            print("\tMensaje original en binario: \t" + txt_to_bin(cipher['cripted_ascii']))


        elif choice == 3:
            break

        else:
            print("Invalid choice")
    

if __name__ == "__main__":
    main()