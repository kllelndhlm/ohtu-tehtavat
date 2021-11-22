import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality'])
            players.append(player)

    def sort_by_points(player):
        return player.points

    sorted_players = sorted(
            players,
            reverse=True,
            key=sort_by_points
        )
    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
