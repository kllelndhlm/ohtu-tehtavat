from player_reader import PlayerReader


def sort_by_points(player):
    return player.points


class Statistics:
    def __init__(self, pelaajaluokanolio):
        self._players = pelaajaluokanolio.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def top_scorers_by_nationality(self, nationality):
        players_of_team = filter(
            lambda player: player.nationality == nationality,
            self._players
        )

        return top_scorers(list(players_of_team))

    def top_scorers(self):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        return result
