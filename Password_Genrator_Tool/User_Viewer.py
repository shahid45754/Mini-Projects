from Pass_importer import Gen,Gen2

User=input("Do you want to Genrate password of 12-digits or 6 digits :'Y' or 'N':-")
    
if User == 'Y' or User == 'y':
        print("Genrating..")
        number=int(input("What password characters you want 12 or 6:-"))
        if number == 12:
            Gen()
        elif number == 6:
            Gen2()
else:
        print("YUS.... No Service!!!")

         



