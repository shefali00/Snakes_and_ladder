import pandas as pd
import random
scores_players={"player 1":0,"player 2":0,"player 3":0,"player 4":0}
win_status_players={"player 1":0,"player 2":0,"player 3":0,"player 4":0}
score_history={"player 1":[],"player 2":[],"player 3":[],"player 4":[]}
dice_history={"player 1":[],"player 2":[],"player 3":[],"player 4":[]}
final_score=0
grid_size=5
while final_score<grid_size*grid_size:
    for player in ["player 1","player 2","player 3","player 4"]:
        dice_roll=random.randint(1,6)
        dice_history[player].append(dice_roll)
        print(f"{player} rolled a {dice_roll}")
        scores_players[player]+=dice_roll
        # if score of aplayer more than 16 then we will not add that score  in scores players and we will duplicate previous value in score history of that player
        if scores_players[player]>grid_size*grid_size:
            score_history[player].append(score_history[player][-1])
            scores_players[player]=score_history[player][-1]
        else:
            score_history[player].append(scores_players[player])
        print(f"{player} has a score of {scores_players[player]}")
        if scores_players[player]==grid_size*grid_size:
            print(f"{player} wins")
            win_status_players[player]=1
            break
    final_score=max(scores_players.values())
#createa data frame to show players (playe 1 , player 2 , player 3 , player 4), dice roll history , position history , win status (0,1)
data={"Players":["Player 1","Player 2","Player 3","Player 4"],
      "Dice Roll History":[dice_history["player 1"],dice_history["player 2"],dice_history["player 3"],dice_history["player 4"]],
      "Position History":[score_history["player 1"],score_history["player 2"],score_history["player 3"],score_history["player 4"]],
      "Win Status":[win_status_players["player 1"],win_status_players["player 2"],win_status_players["player 3"],win_status_players["player 4"]]}
df=pd.DataFrame(data)
print(df)