

def display_match_events(match_data):

    """Display the events of the match"""
    
    print("=" * 40)
    print("MATCH EVENTS")
    print("=" * 40)

    # Get the home and away team information from the match data.
    home_team_id = match_data["teams"]["home"]["id"]
    home_team_name = match_data["teams"]["home"]["name"]

    away_team_id = match_data["teams"]["away"]["id"]
    away_team_name = match_data["teams"]["away"]["name"]

    # Combine starting lineup and substitutes so that all players
    # are available when looking up players by their ID.
    home_team_players = (
         match_data["teams"]["home"]["players"]["starting_lineup"] 
         + match_data["teams"]["home"]["players"]["substitutes"]
         )

    away_team_players = (
         match_data["teams"]["away"]["players"]["starting_lineup"] 
         + match_data["teams"]["away"]["players"]["substitutes"]
         )
    
    # Keep track of the current match period so that the heading 
    # is displayed only when the period changes.
    current_period = None

    for event in match_data["events"]:

            # Display a heading whenever the match moves into a new period.
            if event["period"] != current_period:
                
                current_period = event["period"]

                if current_period == "FH":
                      print("\n========== FIRST HALF ==========")

                elif current_period == "SH":
                      print("\n========== SECOND HALF ==========")

                elif current_period == "ET1":
                     print("\n========== FIRST HALF OF EXTRA TIME ==========")

                elif current_period == "ET2":
                     print("\n========== SECOND HALF OF EXTRA TIME ==========")

            # Process events belonging to the home team.
            if event["team_id"] == home_team_id:

                # Substitutions contain two player IDs: 
                # the player leaving and the player entering the match.
                if event["type"] == "substitution":

                    player_out = None
                    player_in = None

                    # Find both players using their IDs.
                    for player in home_team_players:
                                
                        if event["player_out_id"] == player["id"]:
                            player_out = player

                        if event["player_in_id"] == player["id"]:
                            player_in = player
                            
                    print(
                         f'{event["minute"]} - {event["type"]}:'
                         f'{player_out["first_name"]} {player_out["last_name"]} ->'
                         f' {player_in["first_name"]} {player_in["last_name"]}'
                         f'({home_team_name})'
                         )

                
                # A captain change also contains two player IDs:
                # the previous captain and the new captain.
                elif event["type"] == "captain_change":

                     old_captain = None
                     new_captain = None

                    # Find both captains using their IDs.
                     for player in home_team_players:
                        
                        if event["old_captain_id"] == player["id"]:
                               old_captain = player

                        if event["new_captain_id"] == player["id"]:
                               new_captain = player

                     print(
                          f'{event["minute"]} - {event["type"]}:' 
                          f'{old_captain["first_name"]} {old_captain["last_name"]} ->' 
                          f' {new_captain["first_name"]} {new_captain["last_name"]}'
                          f'({home_team_name})'
                          )


                # Other events such as goals, yellow cards and own goals
                # contain a single player ID.
                else:

                    if "player_id" in event:

                        for player in home_team_players:

                            if event["player_id"] == player["id"]:

                                print(
                                     f'{event["minute"]} - {event["type"]}: '
                                     f'{player["first_name"]} {player["last_name"]}'
                                     f'({home_team_name})'
                                     )

            # Process events belonging to the away team.
            elif event["team_id"] == away_team_id:

                # Substitutions contain two player IDs:
                # the player leaving and the player entering the match.
                if event["type"] == "substitution":

                        player_out = None
                        player_in = None

                        # Find both players using their IDs.
                        for player in away_team_players:

                            if event["player_out_id"] == player["id"]:
                                 player_out = player

                            if event["player_in_id"] == player["id"]:
                                 player_in = player
                                 
                        print(
                             f'{event["minute"]} - {event["type"]}:'
                             f'{player_out["first_name"]} {player_out["last_name"]} ->'
                             f' {player_in["first_name"]} {player_in["last_name"]}'
                             f'({away_team_name})'
                             )

                # A captain change also contains two player IDs:
                # the previous captain and the new captain.
                elif event["type"] == "captain_change":
                    
                    old_captain = None
                    new_captain = None

                    # Find both captains using their IDs
                    for player in away_team_players:
                    
                        if event["old_captain_id"] == player["id"]:
                            old_captain = player

                        if event["new_captain_id"] == player["id"]:
                            new_captain = player

                    print(
                         f'{event["minute"]} - {event["type"]}:'
                         f'{old_captain["first_name"]} {old_captain["last_name"]} ->'
                         f' {new_captain["first_name"]} {new_captain["last_name"]}'
                         f'({away_team_name})'
                         )

                # Other events such as goals, yellow cards and own goals
                # contain a single player ID.
                else:

                    if "player_id" in event:
                 
                        for player in away_team_players:

                            if event["player_id"] == player["id"]:

                                print(
                                     f'{event["minute"]} - {event["type"]}: '
                                     f'{player["first_name"]} {player["last_name"]}'
                                     f'({away_team_name})'
                                     )