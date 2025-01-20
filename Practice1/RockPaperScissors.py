import random;
# Print statement introducing the Rock Paper Scissors Game
print("Welcome to the Rock, Paper and Scissors Game");

# get_choices function will get the user input and store it as a choice
# this function will also use random library to randomize computer choice option
def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors): ");

    while player_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid option selected, please try again");
        player_choice = input("Enter a choice (Rock, Paper, Scissors): ");

    print("Player selected " + player_choice);
    options = ["Rock", "Paper", "Scissors"];
    computer_choice = random.choice(options);
    choices = {"Player": player_choice, "Computer": computer_choice};
    return choices;

# declare_win function will filter through choices and declare whether the player won or lost
def declare_win(player, computer):
    if(player == computer): 
        return "Player and Computer Tied";
    elif ((player == "Rock" and computer == "Paper") or
      (player == "Scissors" and computer == "Rock") or
      (player == "Paper" and computer == "Scissors")):
        return "Player Lost";
    else: 
        return "Player Won";

# Here is where the functions are called and finally the results are printed.
choices = get_choices();
print("Computer picked: " + choices["Computer"]);
win_status = declare_win(choices["Player"], choices["Computer"]);
print(win_status);