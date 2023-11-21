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

def scan(str):
    a = {}
    for letter in str:
        if letter not in a.keys():
            a[letter] = str.count(letter)
    return a

def play(ans, lives):
    quit = False
    win = False
    counts = scan(ans)
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
            #green boxes and black boxes:
            for i in range(len(guess)):
                if guess[i] == ans[i]:
                    reply.append("🟩")
                    counts[guess[i]] -= 1
                elif guess[i] in ans:
                    reply.append("?")
                else:
                    reply.append("⬛")
            #yellow boxes + capable of handling duplicate words:
            for k in range(len(guess)):
                if reply[k] == "?":
                    if counts[guess[i]] > 0:
                        reply[k] = "🟨"
                        counts[guess[i]] -= 1
                    else:
                        reply[k] = "⬛"
            #print reply:
            for j in range(len(reply)):
                print(reply[j], end="")
            lives -= 1
    if win == True:
        print("You win!")
    elif lives == 0: 
        print("Out of lives!")
    else:
        print("Break from game")
        quit = True
    return quit

def main():
    print("Welcome to my own wordle")
    inp = input("(enter to play, type \'q\' to break, type \'*\' to show answer): ")
    if inp == "":
        debug_mode = False
        quit = False
    elif inp == "*":
        debug_mode = True
        quit = False
        print("enter cheating mode")
    else:
        quit = True
    while quit == False:
        answer = pickword(readfile("words.txt"))
        if debug_mode == True:
            print(answer)
        quit = play(answer, 6)
    print("Break from program")

main()

