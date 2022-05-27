info = input().split(" ")
a_players = 0
b_players = 0
players_per_team_a = 11
players_per_team_b = 11
player_loses = []
for card in info:
    if card not in player_loses:
        player_loses.append(card)
        if "A" in card:
            a_players += 1
            players_per_team_a -= 1
        elif "B" in card:
            b_players += 1
            players_per_team_b -= 1
        if players_per_team_a < 7 or players_per_team_b < 7:
            break
print(f"Team A - {11 - a_players}; Team B - {11 - b_players}")
if players_per_team_a < 7 or players_per_team_b < 7:
    print("Game was terminated")
