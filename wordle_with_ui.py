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
    def submit(self):
        guess = self.AttemptInput.text()
        if len(guess) != 6:
            message = QMessageBox()
            message.setText("Invalid guess length")
            message.exec()
        elif not guess.isalpha():
            message = QMessageBox()
            message.setText("Guess must only contain letters")
            message.exec()
        else:
            lives = 6
            win = False
            counts = scan(ans)
            if win == False and lives > 0:
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
                            if counts[guess[i]] > 0:
                                reply[k] = "🟨"
                                counts[guess[i]] -= 1
                            else:
                                reply[k] = "⬛"
                    #print reply:
                    reply_str = self.MainDisplay.text() + "\n"
                    result_str = ""
                    for j in range(len(reply)):
                        result_str += reply[j]
                    self.MainDisplay.setText(reply_str + result_str)
                    lives -= 1
            if win == True:
                self.MainDisplay.setText(self.MainDisplay.text() + "\n🟩🟩🟩🟩🟩🟩\nYou Win!")
            elif lives == 0: 
                self.MainDisplay.setText(self.MainDisplay.text() + "Out of lives!")
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

ans = pickword(readfile("words.txt"))
print(ans)
main()
