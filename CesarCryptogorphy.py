print("david longshore")

def main():
    print("chose one option ")
    choice=int(input("1.encryption \n2.decryption"))
    if choice==1:
        encryption()
    elif choice==2:
        decryption()
    else:
        print("Wrong choice buddy")

def encryption():
    print("Encryption")
    message=input("Enter your message here: ")
    key=int(input("Enter key (1-94)"))
    encryptedtext=""
    for i in range(len(message)):
        temp=(ord(message[i])+key)
        if temp>126:
            temp=temp-127+32
        encryptedtext+=chr(temp)
    print("Encrypted "+encryptedtext)
    main()

def decryption():
    print("Decryption")
    print("Message can only be lower or uppercased.")
    encryptedmessage=input("Enter the encrypted text:")
    decryptkey=int(input("Enter encryption key"))
    decryptedtext=""
    for i in range(len(encryptedmessage)):
        temp=(ord(encryptedmessage[i])-decryptkey)
        if temp<32:
            temp=temp+127-32
        decryptedtext+=chr(temp)
    print("Decrypted "+decryptedtext)

if __name__ == "__main__":
    main()