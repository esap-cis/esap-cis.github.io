# Tour de Sim 

Summary of deliverables:

- nba\_simulation.py
- readme\_nba\_sim.txt

## 0. Getting Started

### A. Goals
The goal of this assignment is to simulate the outcomes of a real-world tournament using probability and randomness. Specifically:

* Practice using `random` module functions (e.g. `random.random()`, `random.choices()`)
* Apply concepts of probability and expected value
* Write code that mirrors real-world processes
* Think critically about modeling assumptions

### B. Motivation
The NBA Playoffs are one of the most-watched sports tournaments in the world. Behind each game is uncertainty: who will win? How far will a team go? We can use Python to simulate this.

By assigning probabilities to each matchup, we can run simulations of the entire playoffs over and over to estimate:

* The chance a team wins a series
* The probability a team wins the championship
* The expected number of games played

By using the **Monte Carlo method**, we can simulate and approximate the values above without needing to wade in the math for too long. Although, mathematical reasoning will derive the same result, as computer scientists, we can try different methods using a different set of tools and skills to acheive the same thing.


### C. Overview: How the NBA Playoffs Work

The NBA has **30 teams**, but only the top **16 teams** make the playoffs — **8 from the Eastern Conference** and **8 from the Western Conference**. This assignment focuses only on those 16.

The playoffs are structured as a **single-elimination bracket**, where each matchup is a **best-of-7 series**:

* In each conference, teams are **seeded 1 to 8** (based on regular season performance).
* The **first round matchups** are:

  * 1 vs 8
  * 2 vs 7
  * 3 vs 6
  * 4 vs 5
* The winner of each series is the **first team to win 4 games**.
* After each round, the winners advance and play again in another best-of-7 series.
* Each conference eventually produces **one finalist**.
* The **NBA Finals** is the final best-of-7 series between the Eastern and Western conference champions.

So to win the championship, a team must win **4 rounds**, each requiring **up to 7 games**.

Your job is to simulate this entire playoff tournament — thousands of times — and collect statistics about team performance.

## 1. The Simulation

You will write code in `nba_simulation.py` to simulate a single playoff tournament. 

### A) How Strengths Translate to Win Probability

Each team is assigned a **strength**. This is not a probability of winning outright, but a relative weight used to compare against their opponent. To determine the probability that **Team A beats Team B** in a game, use:

$$
P(\text{A wins}) = \frac{s_A}{s_A + s_B}
$$

This ensures that stronger teams have higher chances, and the comparison is always between the two teams facing off. For example:

* If $s_A = 0.7$  and $s_B = 0.25$, then $P(\text{A wins}) = 0.75$
* If both teams have $s = 0.5$, it's a fair 50/50 game

Inside your simulation, use `random.random()` to determine the outcome of each game:

```python
if random.random() < prob_A_wins():
    return teamA
else:
    return teamB
```


### B) Simulation Setup

To get you started, we’ve provided a Python file called `nba_simulation.py` where you’ll write all your code. We’ve also included a pre-populated dictionary of playoff teams and their corresponding strengths in a separate file called `playoff_teams.py`.

This dictionary contains all 16 teams that made the 2024–2025 NBA playoffs: 8 from the Eastern Conference and 8 from the Western Conference. Each team is mapped to a **list containing two values**:

1. **Seed** — the team’s ranking within their conference based on their regular season performance (1 is the best, 8 is the lowest seed to make the playoffs).
2. **Strength** — a numeric value (e.g., 59.3 or 51.5) representing how strong the team is compared to others. See above.

```python
# playoff_teams.py

playoff_teams = {
    "East": {
        "Cleveland Cavaliers":    [1, 56.4],
        "Boston Celtics":         [2, 55.5],
        "New York Knicks":        [3, 53.2],
        "Indiana Pacers":         [4, 53.7],
        "Milwaukee Bucks":        [5, 51.5],
        "Detroit Pistons":        [6, 51.0],
        "Orlando Magic":          [7, 49.5],
        "Miami Heat":             [8, 48.9],
    },
    "West": {
        "Oklahoma City Thunder":  [1, 59.3],
        "Houston Rockets":        [2, 53.2],
        "Los Angeles Lakers":     [3, 51.8],
        "Denver Nuggets":         [4, 53.6],
        "Los Angeles Clippers":   [5, 53.3],
        "Minnesota Timberwolves": [6, 54.2],
        "Golden State Warriors":  [7, 52.4],
        "Memphis Grizzlies":      [8, 52.1],
    }
}
```

### C) How You’ll Use It

* You’ll use this dictionary to access each team’s strength when calculating win probabilities in your simulation.
* You’ll also use the seed numbers to determine first-round matchups (e.g., 1 vs 8, 2 vs 7, etc.).
* This dictionary is **defined globally**, which means it will be available to all of your functions without needing to pass it as a parameter. You can access it directly inside any function.

In short: **this is the foundation of your simulation** — every decision about which team advances depends on the data in this dictionary. Be sure you understand its structure, and feel free to print it out or inspect it while developing your code.


### D) Implementing Pieces of the Tournament

You job is to complete the following functions that will be in the `nba_simulation.py` but will not be implemented. You are free to implement them as you'd like, however, keeping in mind that you don't just need to make sure they're functional, but also that they can be used to find the statistics and probabilities needed. Many of what is written here is also written in the `nba_simulation.py` document but is expanded on here for understanding. 

```python
def simulate_game(team1, team2):
    """
    Simulates a single game between two teams using their strengths.

    Parameters:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.

    Returns:
        str: The name of the team that wins the game.
    """
    # TODO: implement
```
```python
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
```

To keep track of everything needed to calculate outcomes and statistics, you should maintain a dictionary. This dictionary is fully customizable and can be used to record any information you find useful — such as the number of wins per team across all games, total games played, number of upsets, and more. This dictionary will be passed into each of the functions below as a parameter, `statistics`. How you use this, is entirely up to you!


```python
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
```

```python
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
```

```python
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
```

```python
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
```

## 2. Testing Your Code

A major goal of this assignment is to get practice writing **modular code** in addition to getting exposure to probability and simulation. This means breaking your program into clear, independent parts — each responsible for a specific task.

In this case, you're simulating an NBA playoff tournament. That involves:

* Simulating a single **game**
* Simulating a **series** (best of 7 games)
* Simulating a **round** (multiple matchups)
* Simulating an entire **tournament**
* Running that tournament simulation **multiple times** and tracking results

Each of these should be implemented as its own **function**, with well-defined inputs and outputs. This makes it easier to **test** parts of your code before trying to get everything working at once.

For example, once you've written `simulate_game(team1, team2)`, you can test it on just two teams to see how often one wins over the other. Once you're confident that works, you can move on to `simulate_series(...)`, and so on.

To help organize your code, you can write a special function called `main()`. This function serves as your testing ground. It lets you run custom simulations, print out results, or debug any of your code in a controlled way. For example:

```python
def main():
    winner = simulate_series("Celtics", "Bulls", statistics={})
    print("Series Winner:", winner)
```

At the bottom of your file, add the following so Python knows to run your `main()` only when the file is executed directly:

```python
if __name__ == "__main__":
    main()
```

This setup keeps your code clean and modular — and gives you a flexible way to test as you go.


## 3. Putting It Together

Now, after you've implemented the functions that will do most of the heavy lifting in simulating the tournament, it's time to implement the *drivers*, that is, the functions that will use those functions above to, well drive the simulation forward. We'll need you to implement a `simulate_tournament()` function which will simulate the entire NBA playoff and returns the championship winner exactly how it is written as a `key` in the dictionary mapping `teams` to `strengths`. 

```python
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

```

> Once you've finished writing the function to simulate a single tournament, you can now implement the final function, which runs the tournament simulation `n` times and uses the returned statistics to update any running totals across all simulations.



```python
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
```



## 4. Final Deliverables

In your README, answer the following:

What are some assumtions used in our simulation?


### Main Statistics
1. What is the probability the **Oklahoma City Thunder** sweep their first series (win 4–0)?
2. What is the probability the **Oklahoma City Thunder** win the championship?
3. What is the expected number of games the **Indiana Pacers** lose in a single playoff run?
4. In 10,000 simulations, how many times do the **Oklahoma City Thunder** face the **Indiana Pacers** in the Finals?
5. Which team causes the **most upsets** across all simulations?
6. Which team had the **highest chance of winning** *given* they reached the Finals?


### Optional Statistics

In case you finish the assignment sooner, here are more statistics that are bit more interesting than those above and can be more descriptive about the tournament as a whole.

* What is the **average number of games per series** across all playoffs?
* What is the **average total number of games** in an entire tournament?
* How often does a **Game 7** occur? Which team is **most likely to lose in Game 7**?
* How often does an **8th seed beat a 1st seed**?
* Which team **most often loses in the Finals**?
* How often do **both 1-seeds reach the Finals**?
* Pick **two teams**. How often does one eliminate the other?
* Pick **two teams**. How often do they meet in the playoffs?
* Pick **any team**. What’s their **conditional probability of winning** the championship *given* they made it to the Finals?
