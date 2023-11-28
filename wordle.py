import random as rand


def readfile(path):
    with open(path, "r") as f:
        words = f.readlines()
    return words


def pickword(words):
    ans = rand.choice(words)
    return ans.lower().strip("\n")


def ask():
    error = True
    while error:
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


def scan(s: str):
    a = {}
    for letter in s:
        if letter not in a.keys():
            a[letter] = s.count(letter)
    return a


def play(ans, lives) -> bool:
    _quit = False
    win = False
    counts = scan(ans)
    while not win and lives > 0:
        print("\nLives: ", lives)
        guess = ask()
        if guess == "q":
            break
        elif guess == ans:
            win = True
        else:
            reply = []
            # green boxes and black boxes:
            for i in range(len(guess)):
                if guess[i] == ans[i]:
                    reply.append("🟩")
                    counts[guess[i]] -= 1
                elif guess[i] in ans:
                    reply.append("?")
                else:
                    reply.append("⬛")
            # yellow boxes + capable of handling duplicate words:
            for k in range(len(guess)):
                if reply[k] == "?":
                    if counts[guess[i]] > 0:
                        reply[k] = "🟨"
                        counts[guess[i]] -= 1
                    else:
                        reply[k] = "⬛"
            # print reply:
            for j in range(len(reply)):
                print(reply[j], end="")
            lives -= 1
    if win:
        print("You win!")
    elif lives == 0:
        print("Out of lives!")
    else:
        print("Break from game")
        _quit = True
    return _quit


def playgame():
    print("Welcome to my own wordle")
    inp = input("(enter to play, type \'q\' to break, type \'*\' to show answer): ")
    if inp == "":
        debug_mode = False
        _quit = False
    elif inp == "*":
        debug_mode = True
        _quit = False
        print("enter cheating mode")
    else:
        _quit = True
    while not _quit:
        answer = pickword(readfile("words.txt"))
        if debug_mode:
            print(answer)
        _quit = play(answer, 6)
    print("Break from program")


if __name__ == "__main__":
    playgame()
