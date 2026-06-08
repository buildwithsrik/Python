class MultiFunctions():
    
    def Subfields ():
        AISubFields=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print(" Sub-fields in AI are:\n",
          AISubFields[0],"\n",
          AISubFields[1],"\n",
          AISubFields[2],"\n",
          AISubFields[3],"\n",
          AISubFields[4],"\n",
          AISubFields[5])

    def OddEven ():
        a=int(input("Enter a number :"))
        if(a % 2 == 0):
           print(a, "is Even number")
        else:
           print(a, "is odd number")

    def Eligible():
        G = input("Your Gender:")
        g = G.lower()
        A = int(input("Your Age:"))
        if(g=='male' and A >= 21):
            print(" Your Gender:", G,"\n",
              "Your Age:",A,"\n",
              "Eligible")
        elif((g=='female' and A >= 18)):
            print(" Your Gender:", G,"\n",
              "Your Age:",A,"\n",              
              "Eligible")
        else:
            print(" Your Gender:", G,"\n",
              "Your Age:",A,"\n",
              "NotEligible")

    def percentage():
        Subject1= int(input("Enter Subject1 Mark:"))
        Subject2= int(input("Enter Subject2 Mark:"))
        Subject3= int(input("Enter Subject3 Mark:"))
        Subject4= int(input("Enter Subject4 Mark:"))
        Subject5= int(input("Enter Subject5 Mark:"))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=Total/5
        print("Subject1=",Subject1, "\n"
        "Subject2=",Subject2, "\n" 
        "Subject3=",Subject3, "\n"
        "Subject4=",Subject4, "\n" 
        "Subject5=",Subject5, "\n"
        "Total : ", Total,"\n"
        "Percentage : ", float(Percentage))

    def triangle():
        TH=int(input("Enter Height:"))
        TB=int(input("Enter Breadth:"))
        TriangleArea = float((TH*TB)/2)
        PH1=int(input("Enter Height1 for perimeter:"))
        PH2=int(input("Enter Height2 for perimeter:"))
        PB=int(input("Enter Breadth for perimeter:"))
        Perimeter=PH1+PH2+PB
        print("Height:",TH)
        print("Breadth:",TB)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", TriangleArea)
        print("Height1:",PH1)
        print("Height2:",PH2)
        print("Breadth:",PB)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Perimeter)