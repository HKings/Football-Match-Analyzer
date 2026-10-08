from json_loader import load_match_data
from match import display_match_info
from match import display_teams
from events import display_match_events


def main():
    print("=" * 40)
    print("Football Match Analyzer")
    print("=" * 40)

    match_data = load_match_data()

    display_match_info(match_data)

    display_teams(match_data)

    display_match_events(match_data)


if __name__ == "__main__":
    main()
