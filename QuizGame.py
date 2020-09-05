import QuizApp

GameQuestions = [QuizApp.Game1, QuizApp.Game2, QuizApp.Game3, QuizApp.Game4, QuizApp.Game5]
print(GameQuestions)

# Final Result of the Quiz Game

if QuizApp.score <=1:
    print("your total score is: ", QuizApp.score, "-you're Failed, please try again.")

elif QuizApp.score == 2 or QuizApp.score == 3:
    print("you're total Score is: ", QuizApp.score, "-you're almost there. One last chance.")
else:
    print("your total score is: ", QuizApp.score, "-Awesome, You cleared the Quiz Game. Congratulations!!")


