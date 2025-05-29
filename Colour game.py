from tkinter import *
import random
import time

colours = ["Red", "Blue", "Green", "Pink", "Black", "Yellow", "Orange", "Purple", "Brown"]
score = 0
timeLimit = 30
highScore =0
startTime = None

root = Tk()
root.title("Color Game")
root.geometry("1500x900")

label = Label(root, font=('Helvetica', 96))
label.pack(pady=20)

entry = Entry(root)
entry.pack()
entry.focus_set()

scoreLabel = Label(root, text="Score: 0")
scoreLabel.pack()

highScoreLabel = Label(root, text="High score: 0")
highScoreLabel.pack()

restartBtn = Button(root, text="Restart", command=lambda: restart())
restartBtn.pack(pady=10)

def nextColor():
    global score, startTime, highScore
    if time.time() - startTime > timeLimit:
        label.config(text="Time's up!", fg="black")
        entry.config(state=DISABLED)
        if score>highScore:
            highScore=score
            highScoreLabel.config(text=f"High score: {highScore}")
        return
    
    typed = entry.get().strip()
    if typed.lower() == label.cget("fg").lower():
        score += 1
        scoreLabel.config(text=f"Score: {score}")

    entry.delete(0, END)
    text = random.choice(colours)
    color = random.choice(colours)
    label.config(text=text, fg=color)

    root.after(2000, nextColor)  # Wait 1 second before next round

def restart():
    global score, startTime
    score=0
    startTime = time.time()
    scoreLabel.config(text="Score: 0")
    entry.config(state=NORMAL)
    entry.delete(0, END)
    entry.focus_set()
    nextColor()

restart()
root.mainloop()