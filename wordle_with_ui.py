from PyQt6.QtWidgets import *
from PyQt6 import uic
import random as rand

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("wordle_ui.ui", self)
        self.show()
        self.StartButton.clicked.connect(self.start)
        self.AttemptSubmit.clicked.connect(self.submit)
    def start(self):
        self.MainDisplay.setEnabled(True)
        self.AttemptInput.setEnabled(True)
        self.AttemptSubmit.setEnabled(True)
        self.StartButton.setEnabled(False)
    def submit(self):
        guess = self.AttemptInput.text().lower()
        if len(guess) != 6:
            message = QMessageBox()
            message.setText("Invalid guess length")
            message.exec()
        elif not guess.isalpha():
            message = QMessageBox()
            message.setText("Guess must only contain letters")
            message.exec()
        else:
            guess_spaced = ""
            for m in range(len(guess)):
                guess_spaced += guess[m].upper() + " "
            reply_str = self.MainDisplay.text() + "\n"
            self.MainDisplay.setText(reply_str + guess_spaced.strip())
            win = False
            counts = scan(ans)
            global life
            if win == False and life > 0:
                if guess == ans:
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
                            if counts.get(guess[k], 0) > 0:
                                reply[k] = "🟨"
                                counts[guess[k]] -= 1
                            else:
                                reply[k] = "⬛"
                    #print reply:
                    result_str = ""
                    for j in range(len(reply)):
                        result_str += reply[j]
                    self.MainDisplay.setText(reply_str + guess_spaced.strip() + "\n" + result_str)
                    #self.MainDisplay_2.setText(self.MainDisplay_2.text() + guess_spaced.strip() + "\n\n\n")
                    life -= 1
            if win == True:
                self.MainDisplay.setText(self.MainDisplay.text() + "\n🟩🟩🟩🟩🟩🟩\n" + "\nYou Win!")
            elif life == 0: 
                self.MainDisplay.setText(self.MainDisplay.text() + "\n" + ans +"\nOut of lives!")
def scan(str):
    a = {}
    for letter in str:
        if letter not in a.keys():
            a[letter] = str.count(letter)
    return a

def readfile(path):
    with open(path, "r") as f:
        words = f.readlines()
    return words
def pickword(words):
    ans = rand.choice(words)
    return ans.strip("\n")

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

life = 6
ans = pickword(readfile("words.txt"))
print(ans)
main()
