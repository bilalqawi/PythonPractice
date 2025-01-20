import random;

print("Welcome to the Rock, Paper and Scissors Game");

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


def declare_win(player, computer):
    if(player == computer): 
        return "Player and Computer Tied";
    elif ((player == "Rock" and computer == "Paper") or
      (player == "Scissors" and computer == "Rock") or
      (player == "Paper" and computer == "Scissors")):
        return "Player Lost";
    else: 
        return "Player Won";

choices = get_choices();
print("Computer picked: " + choices["Computer"]);
win_status = declare_win(choices["Player"], choices["Computer"]);
print(win_status);