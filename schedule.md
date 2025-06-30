# ESAP Computer Science Schedule

This course introduces students to key ideas in programming, data visualization, algorithms, game theory, and web-based applications — all through hands-on projects and strategic problem-solving. Over the span of three weeks, students will develop AI bots, simulate games, and build web systems that connect code to real-world usage cases.

**Note:** This schedule is tentative and subject to change at any time based on instructional needs, pacing, or other factors.

# Week 1: General Python

## Monday – Introduction to Python and PennDraw
### Lecture:
- **Course Introduction**: Overview of course goals, structure, and expectations.
- **Pre-Test**: Quick assessment to gauge prior programming experience.
- **Introduction to PennDraw**: Learn the basics of the PennDraw graphics library.
- **`my_sketch.py` Walkthrough**: Explore and modify a basic drawing script using PennDraw.
### Lab:
- **Rivalry Sketch**: Use PennDraw to create a visual representation of a rivalry (e.g., sports, pop culture, etc.).
- **Work with `my_sketch.py`**: Build and experiment with simple drawing features.

## Tuesday – Graph Theory and Algorithms in Python
### Lecture:
- **Graphs Overview**: Key definitions and terminology (nodes, edges, directed vs. undirected, etc.).
- **Graph Traversal**: Brute Force traversal, Breath First Search, Dijkstras, and more.
- **Paper-Based Exercises**: Solve graph problems by hand to reinforce understanding.

### Lab:
- **Graph Traversals**: Implement Depth-First Search (DFS) and Breadth-First Search (BFS) in Python.
- **Brute Force Search**: Use brute-force techniques to explore graph-based problems.

## Wednesday – Discrete Probability and Simulation

### Lecture:
- **Introduction to Probability**: Define basic concepts like events, outcomes, and sample space.
- **Limit Behavior**: Understand probability as the limit of trials approaching infinity.
- **Logical Combinations**: Explore AND, OR, Mutual Exclusion in probabilistic contexts.
- **Chain Rule**: Introduce basic conditional probability and inference.
- **Expectation**: Learn about average outcomes, both uniform and weighted.
- **Simulation Techniques**: Monte Carlo simulations.

### Lab:
- **Tournament Simulation**: Write a Python simulation for a tournament (e.g., sports, games).
- **Estimate Probabilities**: Use simulations to approximate probabilities of outcomes.


## Thursday – Wordle Solving, Part I
### Lecture:
- **Introduction to Wordle**: Explain rules and structure of the Wordle game.
- **Problem Formalization**: Define the problem space computationally.
- **Solving Strategy**: Develop a basic algorithm to choose the “most probable” word based on feedback.
- **N-gram Strategy**: Discuss maximizing probability using letter pairings or patterns.

### Lab:
- **Algorithm Implementation**: Code the Wordle-solving strategy discussed in class.
- **Performance Tuning**: Begin optimizing algorithm efficiency and guess accuracy.

## Friday – Wordle Solving, Part II
### Lecture:
- **Review and Feedback**: Discuss results from Thursday’s work and share insights.
- **Continued Development**: Refine and extend strategies for improved performance.

### Lab:
- **Further Optimization**: Enhance your algorithm to improve speed and accuracy.
- **Challenge**: Try to solve Wordle in fewer steps on average, using simulation or testing.


# Week 2: Data Visualization & Game Theory – *Path Domination Game*
## Monday – Visualization Foundations

- **Weekly Overview**: Introduction to data visualization and game theory in the context of spatial domination games.
<!-- TODO... -->

## Tuesday – Boards as Graphs
<!-- Came up with some stuff here, but of course, this is your week so change it as you wish! -->
- **Graph-Based Modeling**: Represent tiles as nodes, movements as edges, and pieces as node attributes.
- **Game State Encoding**: Use color, ownership, and state to differentiate piece types.
- **Shortest Path Logic**: Understand how piece interactions are driven by graph traversal.
### Lab 
– **Graph Implementation**: Construct a game playthrough as a graph and implement path-based interactions.

## Wednesday – Strategic Agents & Game Theory
- **Game Theory Concepts**: Introduce payoffs, strategy space, and dominant strategies.
- **Heuristic Evaluation**: Design simple scoring functions for evaluating board positions.
- **Minimax Overview**: Learn the basics of adversarial reasoning and decision trees.
### Lab 
– **Agent Simulation**: Evaluate moves, apply update rules, and implement heuristic scoring.

## Thursday
<!-- Not sure -->


## Friday – Tournament Day
- **Agent Design Recap**: Review common strategies and scoring methods.
- **Tournament Setup**: Explain rules, matchups, and how results will be evaluated.

## Lab 
– **Final Agent Tuning**: Polish agent logic and test on custom boards.
- **Tournament Matches**: Compete in a series of games and visualize results.

# Week 3: Web APIs & Applied Intelligence
## Monday – The Web as a Data Source

### Lecture:
- **Intro to the Web for Programmers**:
  - How the web works (HTTP, URLs, status codes, headers).
  - What is an API? RESTful architecture overview.
- **Fetching Data in Python**:
  - Using `requests` to make GET and POST requests.
  - Parsing HTML and JSON responses.
- **Applications in Games & Visualization**:
  - Public APIs for games, open datasets, or real-time stats.

<!-- Much to be developed here. -->
### Lab:
- **Requesting Real Data**:
  - Fetch data from a public API (e.g., game leaderboards, map data, language models).
- **Web-Driven Game Board**:
  - TBD

## Tuesday – Building Your Own API
### Lecture:
- **Intro to Flask (or FastAPI)**:
  - Serving data from Python.
  - Creating simple endpoints.
- **JSON as a Communication Format**:
  - Serialization and deserialization for game states, move requests, scores.
- **Stateful vs Stateless APIs**:
  - Maintaining sessions or game state across calls.

### Lab:
- **API for the Game**:
  - Build a simple API to expose the board state or accept moves.
  - Create endpoints like `/board`, `/move`, `/status`.
- **Test Clients**:
  - Write a separate script to act as a client agent that calls your API to play the game.

## Wednesday – Agents on the Web
### Lecture:
- **Agents as Services**:
  - Running your game-playing agent as an API service.
  - Accepting state, returning the next move.
- **Inter-agent Communication**:
  - How agents can play against each other through web APIs.
  - Design challenges: latency, fairness, validation.

### Lab:
- **Agent-as-a-Service**:
  - Turn your game agent into a Flask API that can be queried for moves.
  <!-- Just like how AI agents on chess.com aren't literal javascript in the web-browser  -->
  - Use POST requests to pass the current board state and receive a move.
- **Tournament Server**:
  - Create a central referee script that queries two agents and runs a match.

## Thursday – Bringing It All Together

### Lecture:
- **Capstone Project Kickoff**:
  - Pitch: Use everything you've built — graph models, visualization, agents, and APIs — to create an **interactive or networked game system**.
  - Ideas:
    - A web-based simulation of your game with live visual updates.
    - Multiplayer agents competing via APIs.
    - A dashboard visualizing game statistics pulled from API logs as agents or players progress.

### Lab:
- **Capstone Sprint Day 1**:
  - Choose your project direction.
  - Set up API, agent, and visualization components.
  - Begin integrating previous work (graph traversal, visualization, strategies).

<!-- Is there a show case? -->
## Friday – Capstone Project Showcase
### Lecture:
- **Presenting Projects**:
  - Students explain architecture, strategy, visualization, and results.
  - Discussion on challenges faced with APIs and coordination.
- **Reflection on Learning**:
  - What it means to design modular, interactive software systems.
  - Real-world analogs: online games, AI services, data dashboards.
