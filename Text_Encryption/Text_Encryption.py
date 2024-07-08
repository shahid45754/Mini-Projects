def encrypt(Text,Shift):
    if Text == Text:
        Lower=Text.lower()
        
        
        
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    en=''
    for i in Lower:
        index=(alpha.index(i)+shift)%len(alpha)
        en+=alpha[index]
        
    print(f"This is your encrypted text:-{en}")

def decrypt(Text,Shift):
    if Text == Text:
        Uppler=Text.lower()
    
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    de=''
    for i in Uppler:
        index=(alpha.index(i)-shift)%len(alpha)
    
    print(f"The Decrypted Text is:{de}")
    
    
User_text=input("What is your text that you want to encrypt:")
shift=int(input("What is your shift values:"))
Choose=input("Type 'En' or 'De' for Operations:")
if Choose == 'En':
    encrypt(User_text,shift)
elif Choose == 'De':
    decrypt(User_text,shift)
else:
    print("Type Proper Choice !!!")
encrypt(User_text,shift)
