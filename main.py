from tkinter.font import BOLD
import turtle as trtl
from turtle import *
import tkinter as tk
from tkinter import *
import random
import leaderboard as lb
#from ctypes import windll
#windll.shcore.SetProcessDpiAwareness(1) #makes text not blurry

#placing tkinter window in middle of screen
screen = tk.Tk()
appX = 500
appY = 200
windowX = screen.winfo_screenwidth()
windowY = screen.winfo_screenheight()
centerX = int(0.5 * (windowX-appX))
centerY = int(0.5 * (windowY-appY))
playerName = "NULL"
def textinput (title, question):
    global result, screen
    
    screen.geometry(f"{appX}x{appY}+{centerX}+{centerY}")
    screen.title(title)
    #screen.resizable(False, False)
    font = ("Consolas", 20, BOLD)
    questionPlace = tk.Label(screen, text=question, font=font).pack()
    result = tk.Entry(screen, justify=CENTER, font=font)
    result.pack(pady=20)
    enter = tk.Button(screen, text="Enter", command=nameEntered, font=font).pack()
    screen.mainloop()
def nameEntered():
    global screen, playerName
    playerName = result.get()
    screen.destroy()
    
textinput("Welcome To Mastermind", "Enter Your Name:")
wn = trtl.Screen() 

wn.setup(width=0.7, height=0.7)
# insert image code
mastermind_photo = "mastermind.gif"
wn.bgpic(mastermind_photo)

leaderboard_file_name = "leaderboard.txt"
# initilizing turtles
painter = trtl.Turtle()
painter.hideturtle()
painter.speed(0)
red = trtl.Turtle()
red.hideturtle()
green = trtl.Turtle()
green.hideturtle()
blue = trtl.Turtle()
blue.hideturtle()
yellow = trtl.Turtle()
yellow.hideturtle()
brown = trtl.Turtle()
brown.hideturtle()
orange = trtl.Turtle()
orange.hideturtle()
black = trtl.Turtle()
black.hideturtle()
white = trtl.Turtle()
white.hideturtle()
# defining locations of everything
inputStartX = -140
startX = -140.1
startY = -236.5
hLength = 69.38
vLength = 58.7
guessSize = 16
finalStartX = -140.5
finalStartY = 347.8
finalXChange = 71

painter.penup()
painter.goto(startX,startY)
def drawingButtons(x,y,color):
    color.penup()
    color.speed(0)
    color.shape("circle")
    color.shapesize(3)
    color.goto(x,y)
    color.showturtle()
#drawing buttons
red.color("red")
green.color("green")
blue.color("blue")
yellow.color("yellow")
brown.color("#957045") #brown/gold color
orange.color("orange")
black.color("black")
white.color("white")
#drawing input buttons
allColors = [red, green, blue, yellow, brown, orange, black, white]
placed = 0 #amount of input buttons placed
for color in allColors:
    if (placed < 4):
        drawingButtons(inputStartX+(92*placed), -290, color)
    else:
        drawingButtons(inputStartX+(92*(placed-4)), -368, color)
    placed+=1

def drawingHint(x,y,factor,color):
    painter.penup()
    painter.goto(x,y+factor)
    painter.fillcolor(color)
    painter.begin_fill()
    painter.pendown()
    painter.pencolor("white")
    painter.circle(8)
    painter.end_fill()    
    painter.penup()


#choose and randomized colors
colorBank = ["red", "green", "blue", "yellow", "brown", "orange", "black", "white"]
storedColorBank = colorBank[:]
guesses = []
random.shuffle(colorBank)
i = 0
for i in range (4):
    colorBank.pop()
won = False
colorBank = ["brown", "orange", "red", "white"] #hardcode value for testing
storedAnswer = colorBank[:]

def drawAnswer (answer):
    i = 0
    for i in range (4):
        painter.penup()
        if (answer[i] == "brown"):
            painter.fillcolor("#957045")
            painter.color("#957045")
        else:
            painter.pencolor(answer[i])
            painter.fillcolor(answer[i])
        painter.goto(finalStartX+(finalXChange*i), finalStartY)
        painter.pendown()
        painter.begin_fill()
        painter.circle(27)
        painter.end_fill()
        painter.penup()


#game  
guessList = []
factor = 0
guessCount = 1
guess = None
def inputClicked(color):
    global guess
    global notClicked
    notClicked = False
    guess = color
def redClicked(x,y):
    inputClicked("red")
def greenClicked(x,y):
    inputClicked("green")
def blueClicked(x,y):
    inputClicked("blue")
def yellowClicked(x,y):
    inputClicked("yellow")
def brownClicked(x,y):
    inputClicked("brown")
def orangeClicked(x,y):
    inputClicked("orange")
def blackClicked(x,y):
    inputClicked("black")
def whiteClicked(x,y):
    inputClicked("white")
def backspaceClicked():
    global guessList, painter, colorPlaced
    tracer(20)
    undos = 8
    if (len(guessList)>0):
        if (len(guessList) == 1):
            undos = 7
        for i in range (undos):
            painter.undo()
        guessList.pop()
        colorPlaced -=1
    tracer(1)
while (guessCount <= 10):
    rightPositions = 0
    rightColors = 0
    guessList = [] 
    colorPlaced = 0
    while (len(guessList) < 4):
        global notClicked
        notClicked = True
        while (notClicked):
            wn.listen()
            red.onclick(redClicked)
            green.onclick(greenClicked)
            blue.onclick(blueClicked)
            yellow.onclick(yellowClicked)
            brown.onclick(brownClicked)
            orange.onclick(orangeClicked)
            black.onclick(blackClicked)
            white.onclick(whiteClicked)
            wn.onkey(backspaceClicked, "BackSpace")
        guessList.append(guess)
        painter.goto(startX + (hLength*colorPlaced), startY + (vLength*(guessCount-1)))
        if (guess == "brown"):
            painter.fillcolor("#957045")
            painter.color("#957045")
        else:
            painter.fillcolor(guess)
            painter.color(guess)
        painter.begin_fill()
        painter.pendown()
        painter.circle(guessSize)
        painter.end_fill()
        painter.penup()
        colorPlaced+=1
    j = 0
    k = 0 
    while (k < 4):
        if (guessList[k] == colorBank[k]):
            colorBank[k] = "VOID" 
            rightPositions+=1 
        k+=1
    while (j < 4):
        if (guessList[j] in colorBank): 
            rightColors+=1
            index = colorBank.index(guessList[j])
            colorBank[index] = "VOID"

        if (rightPositions == 4):
            won = True
            break
        j+=1
    guessCount+=1

    startHintX = 127.25
    xHintChange = 27.25
    startHintY = -217
    yHintChange = 23
    hintX = startHintX

    if (rightPositions > 0 or rightColors > 0):
        for positionDrawn in range (rightPositions+rightColors):
            if (positionDrawn < rightPositions):
                drawingHint(hintX, startHintY, factor, "red")
            else:
                drawingHint(hintX, startHintY, factor, "white")
            hintX = hintX + xHintChange
            if (positionDrawn+1 == 2):
                hintX = startHintX
                startHintY = startHintY - yHintChange 
    factor+=58.6
    
    colorBank = storedAnswer[:]
    if (won):
        break
# if you lose
def manage_leaderboard():
    global guessCount, won
    score = guessCount-1
    global painter

  # get names and scores from the leaderboard file
    leader_names_list = lb.scoreNameCombo(leaderboard_file_name, "names")
    leader_scores_list = lb.scoreNameCombo(leaderboard_file_name, "scores")

  # show the leaderboard with or without the current player
    if ((len(leader_scores_list) < 5 or score <= leader_scores_list[4]) and won):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, playerName, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, painter, score)
    elif (won):
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, painter, score)
    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, painter, score)
drawAnswer(storedAnswer)
manage_leaderboard() 

wn.mainloop()