import random as rand

def readfile(path):
    with open(path, "r") as f:
        words = f.readlines()
    return words
    
def pickword(words):
    ans = rand.choice(words)
    return ans.strip("\n")

def ask():
    error = True
    while error == True:
        guess = input("Guess: ")
        if guess == "q":
            break
        elif len(guess) != 6:
            print("Invalid guess length")
        elif not guess.isalpha():
            print("Guess must only contain letters")
        else:
            error = False
    return guess.lower()

def play(ans, lives):
    quit = False
    win = False
    while win == False and lives > 0:
        print("")
        print("Lives: ", lives)
        guess = ask()
        if guess == "q":
            break
        elif guess == ans:
            win = True
        else:
            reply = []
            for i in range(len(guess)):
                if guess[i] == ans[i]:
                    reply.append("🟩")
                elif guess[i] in ans:
                    reply.append("🟨")
                else:
                    reply.append("⬛")
            for j in range(len(reply)):
                print(reply[j], end="")
            lives -= 1
    if win == True:
        print("You win!")
    elif lives == 0: 
        print("Out of lives!")
    else:
        print("Break")
        quit = True
    return quit

def main():
    print("Welcome!")
    print("(enter \'q\' to exit)")
    quit = False
    while quit == False:
        answer = pickword(readfile("words.txt"))
        print(answer)
        quit = play(answer, 6)

main()

