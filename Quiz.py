def new_game():
    guesses=[]
    qstn_num=1
    correct_guesses=0
    for key in qstns:
        print("-------------------------------------")
        print(key)
        for i in options[qstn_num-1]:
           print(i)
        guess=input("Enter A,B,C or D:").upper()
        guesses.append(guess)
        correct_guesses+=check_answer(qstns.get(key),guess)
        qstn_num+=1
    display_score(correct_guesses,guesses)
        
def check_answer(answer,guess):
    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
def display_score(correct_guesses,guesses):
    print("--------------------\nRESULTS:\n---------------------")
    print("Answers:",end=" ")
    for i in qstns:
        print(qstns[i],end=" ")
    print("\nGuesses:",end=" ")
    for j in guesses:
        print(j,end=" ")
    print()

    score=(correct_guesses/len(qstns)*100)
    print("Your score is:",score,"%")

def play_again():
    response=input("Do u wanna play again (yes/no):").upper()
    if response=='YES':
        return True
    else:
        return False
    
qstns={"Who created python?":"A","Year python was created?":"C","Is Earth round?":"A"}
options=[["A.Guido Vann Rosum","B.Elon Musk","C.Bill Gates"],["A.1998","B.1999","C.1991"],["A.Yes","B.No"]]
new_game()
while play_again():
    new_game()
print("Byeeeeee!")
    


