questions =["What is the capital of France?","Which planet is known as the Red Planet?","Who wrote \"To Kill a Mockingbird\"?","What is the largest ocean on Earth?","Who painted the Mona Lisa?"]

options=["1. Berlin", "2. Madrid","3. Paris","4. Rome"],["1. Earth","2. Mars","3. Jupiter","4. Venus"],["1. Harper Lee","2. Mark Twain","3. J.K. Rowling","3. F. Scott Fitzgerald"],["1. Atlantic Ocean","2. Indian Ocean","3. Arctic Ocean","4. Pacific Ocean"],["1. Vincent van Gogh","2. Pablo Picasso","3. Leonardo da Vinci","4. Claude Monet"]

answers=["3. Paris","2. Mars","1. Harper Lee","4. Pacific Ocean","3. Leonardo da Vinci"]

# def kbc():
#     for i in range(0,5):
#        print( questions[i])
#        sub=options[i]
#     for r in sub:
#             print(r)
#             value=int(input("Enter your choice:"))
#        if (sub[value]==answers[i]):
#               print ("you won")
#        else:
#             print("you lost")
     

# kbc()
# sub= options[0]

# print(sub[0])
# def kbc():
#  money=0
# for i in range(0,5):
#     print(questions[1])
#     sub=options[i]
#     for values in sub:
#         print(values)
#     x=int(input("Enter your choice:"))
#     if(sub[x-1]==answers[i]):
#         print("you won")
#         money=money+10
#         print("your winning prize is:",money,"lakh")
#         if(i<4):
#             print("Question NO.",i+2)
        
#     else:
#         print("you lost")
#         print("your total winning prize is",money,"lakh")
#         break
    
money=0
for i in range(0,5):
    print(questions[1])
    sub=options[i]
    for values in sub:
        print(values)
    x=int(input("Enter your choice:"))
    if(sub[x-1]==answers[i]):
        print("you won")
        money=money+10
        print("your winning prize is:",money,"lakh")
        if(i<4):
            print("Question NO.",i+2)
        
    else:
        print("you lost")
        print("your total winning prize is",money,"lakh")
        break