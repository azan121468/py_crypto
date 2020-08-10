from cryptography.fernet import Fernet

def main():
    print("Select your choice")
    print("1. Encryption")
    print("2. Decryption")
    print("Enter your choice : ",end=" ")
    choice=input()
    if choice=="1":
        print("Enter your message : ",end=" ")
        msg=input()
        key = Fernet.generate_key()
        f = Fernet(key)
        cipher_text=f.encrypt(bytes(msg,'utf-8'))
        print("Key : ",key)
        print("Cipher text : ",cipher_text)
        pass
    elif choice=="2":
        #decryption
        print("Enter your encrypted message : ",end=" ")
        encrypted_msg=bytes(input(),'utf-8')
        print("Enter your key : ",end=" ")
        key=bytes(input(),'utf-8')
        f=Fernet(key)
        decrypted_msg=f.decrypt(encrypted_msg)
        print(decrypted_msg)
    else:
        print("invalid")

main()
