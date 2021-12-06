import requests

class PlayerReader:
    def __init__(self, urli):
        self._url = urli

        response = requests.get(self._url).json
        print(response)
        players = []


#        for player_dict in response:
 #           player = [player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality']]
  #          players.append(player)
#
 #       return players
