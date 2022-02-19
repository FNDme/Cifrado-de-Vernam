import random

def txt_to_bin(txt):
    return ''.join('{0:08b}'.format(ord(x), 'b') for x in txt)

def bin_to_txt(bin):
    return ''.join(chr(int(bin[i:i+8], 2)) for i in range(0, len(bin), 8))

def keygen(length):
    random.seed()
    key = ""
    for i in range(length):
        temp = random.randint(0, 1)
        key += str(temp)
    return key

def encrypt(txt):
    bin_txt = txt_to_bin(txt)
    temp = dict()
    temp['cripted_bin'] = ""
    temp['key_bin'] = keygen(len(bin_txt))
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

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, txt):
    with open(filename, 'w') as f:
        f.write(txt)


# def menu():
#     print("""
#     1. Encrypt
#     2. Decrypt
#     3. Exit
#     """)
#     choice = int(input("Enter your choice: "))
#     return choice

# def work_with_files():
#     print("""
#     1. Files
#     2. Text
#     3. Exit
#     """)
#     choice = int(input("Enter your choice: "))
#     return choice

# def main():
#     while True:
#         files = work_with_files()
#         if files == 3:
#             break
#         elif files != 1 and files != 2:
#             print("Invalid choice")
#         else:
#             while(True):
#                 choice = menu()
#                 if choice == 1:
#                     if files == 1:
#                         file = input("Enter the file name: ")
#                         with open(file, 'r') as f:
#                             txt = f.read()
#                         txt = txt.replace("\n", "")
#                         cipher = encrypt(txt)
#                     else:
#                         txt = input("Enter text: ")
#                         cipher = encrypt(txt)
#                     print("Cipher (bin): ", cipher['cripted'])
#                     print("Cipher (text): ", bin_to_txt(cipher['cripted']))
#                     print("Key: ", cipher['key'])
#                     print("Do you want to save cipher text to file? (y/n)")
#                     save = input()
#                     if save == 'y' or save == 'Y' or save == 'yes' or save == 'Yes' or save == 'YES':
#                         with open("cipher.txt", 'w') as f:
#                             f.write(cipher['cripted'])
#                         with open("key.txt", 'w') as f:
#                             f.write(cipher['key'])
#                     else:
#                         print("not saved")
#                 elif choice == 2:
#                     cipher = dict()
#                     if files == 1:
#                         file = input("Enter the file name: ")
#                         with open(file, 'r') as f:
#                             cipher['cripted'] = f.read()
#                         print("Is the key in a file? (y/n)")
#                         fileKey = input()
#                         if fileKey == 'y' or fileKey == 'Y' or fileKey == 'yes' or fileKey == 'Yes' or fileKey == 'YES':
#                             file = input("Enter the file name: ")
#                             with open(file, 'r') as f:
#                                 cipher['key'] = f.read()
#                         else:
#                             cipher['key'] = input("Enter the key: ")
#                     else:
#                         cipher['cripted'] = input("Enter cipher: ")
#                         cipher['key'] = input("Enter key: ")
#                     print("decription: ", bin_to_txt(decrypt(cipher)))
#                 elif choice == 3:
#                     break
#                 else:
#                     print("Invalid input")
#             break

# main()        