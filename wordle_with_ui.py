from PyQt6.QtWidgets import *
from PyQt6 import uic
import random as rand
import os
import sys
import time

def resource_path(relative_path):
    #Get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi(resource_path("wordle_ui.ui"), self)
        self.show()
        self.StartButton.clicked.connect(self.start)
        self.AttemptSubmit.clicked.connect(self.submit)
        self.actionExit.triggered.connect(sys.exit)
    def start(self):
        self.MainDisplay.setEnabled(True)
        self.AttemptInput.setEnabled(True)
        self.AttemptSubmit.setEnabled(True)
        self.StartButton.setEnabled(False)
    #happens after you click submit    
    def submit(self):
        guess = self.AttemptInput.text().lower()
        global valid_words
        if len(guess) != 6:
            message = QMessageBox()
            message.setText("Invalid guess length")
            message.exec()
        elif not guess.isalpha():
            message = QMessageBox()
            message.setText("Guess must only contain letters")
            message.exec()
        elif guess not in valid_words:
            message = QMessageBox()
            message.setText("Word not in dictionary")
            message.exec()
        else:
            #print attempted word first
            guess_spaced = ""
            for m in range(len(guess)):
                guess_spaced += guess[m].upper() + " "
            reply_str = self.MainDisplay.text() + "\n"
            self.MainDisplay.setText(reply_str + guess_spaced.strip())
            #real processing
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
                    for j in reply:
                        result_str += j
                        self.MainDisplay.setText(reply_str + guess_spaced.strip() + "\n" + result_str)
                        #time.sleep(0.3)
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
    return ans.lower().strip("\n")

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

with open("valid_words.txt", "r") as f:
    valid_words = f.readline().split()
life = 6
ans = pickword(readfile(resource_path("words.txt")))
print(ans)
main()