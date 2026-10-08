from utils import get_team_captain


def display_match_info(match_data):
    """
    Displays the main information about the football match
    """

    match = match_data["match"]

    print("=" * 40)
    print("MATCH INFORMATION")
    print("=" * 40)

    print(f"Competition : {match['competition']}")
    print(f"Stage : {match['stage']}")
    print(f"Date : {match['date']}")
    print(f"Kickoff : {match['kickoff']}")
    print(f"Match : {match['home_team']} vs {match['away_team']}")
    print(f"Result : {match['home_score']} - {match['away_score']}")
    print(f"Status : {match['status']}")
    print(f"Venue : {match['venue']}")
    print(f"City : {match['city']}")
    print(f"Country : {match['country']}")
    print(f"Referee : {match['referee']}")


def display_teams(match_data):
    """
    Displays teams information and players.
    """

    teams = match_data["teams"]

    for side in ["home", "away"]:

        team = teams[side]

        print("\n" + "=" * 50)
        print(team["name"].upper())
        print("=" * 50)

        print(f"Coach:     {team['coach']}")
        print(f"Formation: {team['formation']}")

        captain_name = get_team_captain(team)
        print(f"Captain: {captain_name}")

        print("\nStarting Lineup")
        print("-" * 30)

        for player in team["players"]["starting_lineup"]:
            print(
                f"# {player['number']:>2} "
                f"{player['display_name']} - "
                f"{player['position']} "
            )

        print("\nSubstitutes")
        print("-" * 30)

        for player in team["players"]["substitutes"]:
            print(
                f"# {player['number']:>2} "
                f"{player['display_name']} - "
                f"{player['position']} "
            )
