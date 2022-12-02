player_score = 0

with open("input.txt", "r") as turns:

    for turn in turns:
        opponent_choice = turn[0]
        end = turn[2]
        player_choice = ""
        if end == "X":
            if opponent_choice == "A":
                player_choice = "Z"
            elif opponent_choice == "B":
                player_choice = "X"
            else:
                player_choice = "Y"
        elif end == "Y":
            if opponent_choice == "A":
                player_choice = "X"
            elif opponent_choice == "B":
                player_choice = "Y"
            else:
                player_choice = "Z"
        else:
            if opponent_choice == "A":
                player_choice = "Y"
            elif opponent_choice == "B":
                player_choice = "Z"
            else:
                player_choice = "X"

        if player_choice == "X" and opponent_choice == "A":
            player_score += 3
        elif player_choice == "Y" and opponent_choice == "B":
            player_score += 3
        elif player_choice == "Z" and opponent_choice == "C":
            player_score += 3
        else:
            if player_choice == "X" and opponent_choice == "C":
                player_score += 6
            if player_choice == "Z" and opponent_choice == "B":
                player_score += 6
            if player_choice == "Y" and opponent_choice == "A":
                player_score += 6
        if player_choice == "X":
            player_score += 1
        if player_choice == "Y":
            player_score += 2
        if player_choice == "Z":
            player_score += 3

print(player_score)
