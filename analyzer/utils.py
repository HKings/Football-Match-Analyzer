def get_team_captain(team):
    """
    Returns the captain´s display mane for a team.
    """

    for player in team["players"]["starting_lineup"]:
        if player["captain"]:
            return player["display_name"]

    return "Unknown"


def get_player_by_id(match_data, player_id):
    """
    Returns a player dictionary given its unique player ID.
    Searches both teams, including starting players and substitutes.
    """

    teams = match_data["teams"]

    for side in ["home", "away"]:

        team = teams[side]

        players = (
            teams[side]["players"]["starting_lineup"] +
            teams[side]["players"]["substitutes"]
        )

        for player in players:

            if player["id"] == player_id:
                return player

    return None





