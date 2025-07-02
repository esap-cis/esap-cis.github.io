import random

# Global dictionary of team strengths (example placeholder)
# playoff_teams.py

playoff_teams = {
    "East": {
        "Cleveland Cavaliers":    [1, 56.4],  # Seed 1
        "Boston Celtics":         [2, 55.5],  # Seed 2
        "New York Knicks":        [3, 53.2],  # Seed 3
        "Indiana Pacers":         [4, 53.7],  # Seed 4
        "Milwaukee Bucks":        [5, 51.5],  # Seed 5
        "Detroit Pistons":        [6, 51.0],  # Seed 6
        "Orlando Magic":          [7, 49.5],  # Seed 7
        "Miami Heat":             [8, 48.9],  # Seed 8
    },
    "West": {
        "Oklahoma City Thunder": [1, 59.3],  # Seed 1
        "Houston Rockets":       [2, 53.2],  # Seed 2
        "Los Angeles Lakers":    [3, 51.8],  # Seed 3
        "Denver Nuggets":        [4, 53.6],  # Seed 4
        "Los Angeles Clippers":  [5, 53.3],  # Seed 5
        "Minnesota Timberwolves":[6, 54.2],  # Seed 6
        "Golden State Warriors": [7, 52.4],  # Seed 7
        "Memphis Grizzlies":     [8, 52.1],  # Seed 8
    }
}

def simulate_game(team1, team2):
    """
    Simulates a single game between two teams using their relative strengths.

    Parameters:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.

    Returns:
        str: The name of the winning team.
    """
    # TODO: Implement using probability formula and random.random()
    pass


def simulate_series(team1, team2, statistics):
    """
    Simulates a best-of-7 series between two teams.

    Parameters:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.
        statistics (dict): Dictionary used to track simulation statistics.

    Returns:
        str: The name of the team that wins the series.
    """
    # TODO: Implement series logic (first to 4 wins)
    pass


def simulate_first_round(initial_matchups, statistics):
    """
    Simulates the first round of the NBA playoffs (also known as the quarterfinals).
    Each conference starts with 8 teams; this round reduces each side to 4 teams.

    Parameters:
        initial_matchups (list): List of (team1, team2) tuples for first round matchups.
        statistics (dict): Dictionary used to track simulation statistics.

    Returns:
        list: List of teams that advance to the semifinals.
    """
    # TODO: implement


def simulate_semifinals(matchups, statistics):
    """
    Simulates the semifinals round of the NBA playoffs.
    4 teams per conference compete; 2 per conference advance to the conference finals.

    Parameters:
        matchups (list): List of (team1, team2) tuples from the previous round.
        statistics (dict): Dictionary used to track simulation statistics.

    Returns:
        list: List of teams that advance to the conference finals.
    """
    # TODO: implement

def simulate_conference_finals(matchups, statistics):
    """
    Simulates the conference finals round.
    This determines which team from each conference advances to the NBA Finals.

    Parameters:
        matchups (list): List of (team1, team2) tuples from the semifinals.
        statistics (dict): Dictionary used to track simulation statistics.

    Returns:
        list: List of two teams, one from each conference, who advance to the NBA Finals.
    """
    # TODO: implement

def simulate_nba_finals(final_matchup, statistics):
    """
    Simulates the NBA Finals between the Eastern and Western Conference champions.

    Parameters:
        final_matchup (tuple): A single tuple (team1, team2) representing the two finalists.
        statistics (dict): Dictionary used to track simulation statistics.

    Returns:
        str: The team that wins the NBA Championship.
    """
    # TODO: implement


def simulate_tournament():
    """
    Simulates one full NBA playoff tournament.

    This function initializes a fresh statistics dictionary,
    runs all four rounds of the playoffs and returns the team that wins 
    the championship.

    Assumes a global dictionary `teams` exists, mapping team names to strengths.

    Returns:
        tuple: (winning_team, statistics), where:
            - winning_team (str): The name of the NBA champion.
            - statistics (dict): A dictionary with keys/values used to track data
              such as number of wins, upsets, total games played, etc.
    """
    # TODO: implement


def run_simulations(n):
    """
    Runs the full NBA tournament simulation `n` times and tracks the results.

    For each simulation:
      - Calls `simulate_tournament()` to simulate the full bracket
      - Records the winning team in a results dictionary

    Parameters:
        n (int): The number of times to repeat the tournament simulation

    Returns:
        dict: A dictionary mapping each team name to the number of championships won
              across all simulations and other metrics.
    """
    # TODO: implement
    pass


def main():
    """
    Optional testing ground. Add your own tests or print statements here.
    """
    pass


if __name__ == "__main__":
    main()