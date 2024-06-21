import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=775, height= 500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle_state = turtle.Turtle()
turtle_state.hideturtle()
turtle_state.penup()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
state_list = states # Creating this to insure that guesses are not repeated

game_continue = True
guess = 0

while game_continue:
    answer = screen.textinput(title=f"Guess the state {guess}/50", prompt="What's the state name?").title()
    if answer == "Exit":
        data_dict = {
            "States" : state_list
        }
        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv("states_to_learn.csv")
        break
    for state in state_list:
        if answer == state:
            guess += 1
            guess_state_info = data[data.state == answer]
            x_cor = int(guess_state_info.x)
            y_cor = int(guess_state_info.y)
            turtle_state.goto(x_cor, y_cor)
            turtle_state.write(f"{answer}")
            state_list.remove(answer)  # Removing the state once it has been guessed

            if guess == 50:
                game_continue = False






