# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# set the levels of scoring
bronze_score = 7
silver_score = 5
gold_score = 3
# return names in the leaderboard file
def scoreNameCombo (file_name, type):
    leaderboard_file = open(file_name, "r")
    scoresOrNames = []
    index = 0
    for line in leaderboard_file:
        if (type == "names"):
            index = 0
            ending = ","
        else: #type == "scores"
            index = line.find(",") + 1
            ending = "\n"
        leaderScoreOrName = ""
        while (line[index] != ending):
            leaderScoreOrName = leaderScoreOrName + line[index]
            index+=1
        if (type == "scores"):
            leaderScoreOrName = int(leaderScoreOrName)
        scoresOrNames.append(leaderScoreOrName)
    leaderboard_file.close()
    return scoresOrNames

# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):
  score = player_score
  index = 0
  #loop through all the scores in the existing leaderboard list
  while (index < len(leader_scores)):
    #check if this is the position to insert new score at
    if (player_score <= leader_scores[index]):
      break
    else:
      index = index + 1
  
  # insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)
  # keep both lists at 5 elements only (top 5 players)
  if (len(leader_names) > 5):
    leader_names.pop()
    leader_scores.pop()
  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  index = 0
  #loop through all the leaderboard elements and write them to the the file
  while (index < len(leader_names)):
    leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")
    index = index + 1

  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(won, leader_names, leader_scores, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Consolas", 20, "bold")
  turtle_object.color("black")
  #turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-650,200)
  turtle_object.hideturtle()
  turtle_object.down()
  index = 0

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  turtle_object.write("\t" + "Leaderboard", font=font_setup)
  turtle_object.penup()
  turtle_object.goto(-600,int(turtle_object.ycor())-50)
  turtle_object.write("Rank" + "\t" + "Name" + "\t" + "Score", font=font_setup)
  turtle_object.penup()
  turtle_object.goto(-600,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  while (index < len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-600,int(turtle_object.ycor())-50)
    turtle_object.down()
    index = index + 1
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-600,int(turtle_object.ycor())-100)
  turtle_object.pendown()

  # display message about player making/not making leaderboard
  if (not won):
    turtle_object.write("Sorry!\nYou didn't win.\nMaybe next time!", font=font_setup)
  elif (player_score <= leader_scores[-1]):
    turtle_object.write("Congratulations!\nYou made the leaderboard!\nYou won in " + str(player_score) + " guesses!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the\nleaderboard. Maybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-600,int(turtle_object.ycor())-50)
  turtle_object.pendown()