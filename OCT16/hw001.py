#Grade Calculator

score=int(input("Enter the score:"))
if (score>89):
    print("Grade A")
elif(score>79 and score<90):
    print("Grade B")
elif(score>69 and score<80):
    print("Grade C")
elif (score > 60 and score < 70):
    print("Grade D")
else:
    print("Grade F")


