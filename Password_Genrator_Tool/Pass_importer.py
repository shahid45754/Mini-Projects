import random
MAX_LEN=12

lower_alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                            'z']
upper_alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                            'Z']
Special_Chars=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
                '*', '(', ')', '<']
Numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def Gen():
   
    #TO CREATE AN ARRAY
    Combo=lower_alphabets+upper_alphabets+Special_Chars+Numbers

    ran_lower=random.choice(lower_alphabets)
    ran_upper=random.choice(upper_alphabets)
    ran_Chars=random.choice(Special_Chars)
    ran_num=random.choice(Numbers)

    temp=ran_lower+ran_Chars+ran_num+ran_upper

    for i in range(MAX_LEN-4):
        temp=temp+random.choice(Combo)
        
    print(f"Your password is ready:-{temp}")

def Gen2():
    MAX=6
    Combo=lower_alphabets+upper_alphabets+Special_Chars+Numbers
    
    ran_lower1=random.choice(lower_alphabets)
    ran_upper1=random.choice(upper_alphabets)
    ran_Chars1=random.choice(Special_Chars)
    ran_num1=random.choice(Numbers)

    temp=ran_lower1+ran_Chars1+ran_num1+ran_upper1

    for i in range(MAX-4):
        temp=temp+random.choice(Combo)
        
    print(f"Your password is ready:-{temp}")


