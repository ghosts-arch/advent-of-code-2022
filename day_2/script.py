player_score = 0

with open("input.txt", "r") as turns:

    for turn in turns:
        opponent_choice = turn[0]
        end = turn[2]
        player_choice = ""
        if end == "Y":
            if opponent_choice == "A":
                player_choice = "X"
            elif opponent_choice == "B":
                player_choice = "Y"
            elif opponent_choice == "C":
                player_choice = "Z"
        elif end == "X":
            if opponent_choice == "A":
                player_choice = "Z"
            elif opponent_choice == "C":
                player_choice = "Y"
            elif opponent_choice == "B":
                player_choice = "X"
        else:
            if opponent_choice == "A":
                player_choice = "Y"
            elif opponent_choice == "C":
                player_choice = "X"
            elif opponent_choice == "B":
                player_choice = "Z"

        print(player_choice)
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

        match player_choice:
            case "X":
                player_score += 1
                break
            case "Y":
                player_score += 2
                break
            case "Z":
                player_score += 3
                break

print(player_score)
