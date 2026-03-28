# Fictional Bassoon

## Overview

This project implements fundamental Artificial Intelligence search techniques through two problem domains:

1. Tic-Tac-Toe using adversarial search (Minimax)
2. Maze solving using uninformed and informed search algorithms (BFS, DFS, A*)

The goal is to demonstrate how different AI algorithms approach decision-making and pathfinding problems.

---

## Features

### Tic-Tac-Toe

* Human vs AI gameplay
* AI uses Minimax algorithm
* Always plays optimally

### Maze Solver

* Solves a grid-based maze
* Implements:

  * Breadth First Search (BFS)
  * Depth First Search (DFS)
  * A* Search Algorithm
* Displays paths for each algorithm

---

## Project Structure

```
ai-game-solver/
│
├── main.py
├── requirements.txt
├── README.md
│
├── tic_tac_toe/
│   ├── game.py
│   ├── minimax.py
│   └── play.py
│
├── maze_solver/
│   ├── maze.py
│   ├── bfs.py
│   ├── dfs.py
│   └── astar.py
│
└── report.pdf
```

---

## Installation

1. Clone the repository:

```
git clone https://github.com/DEEZ-BOI/fictional-bassoon
cd fictional-bassoon
```

2. Ensure Python is installed (version 3.8 or above):

```
python --version
```

3. Install dependencies (if any):

```
pip install -r requirements.txt
```

---

## Usage

Run the main file:

```
python main.py
```

You will see a menu:

```
1. Tic Tac Toe
2. Maze Solver
```

Enter your choice to proceed.

---

## Algorithms Used

### Breadth First Search (BFS)

* Explores level by level
* Guarantees shortest path

### Depth First Search (DFS)

* Explores deeply before backtracking
* Does not guarantee optimal path

### A* Search

* Uses heuristic (Manhattan distance)
* More efficient than BFS in many cases

### Minimax Algorithm

* Used in adversarial games
* Maximizes AI’s chances while minimizing opponent’s advantage

---

## Sample Maze

```
S . . #
# . . G
# # . #
```

S = Start

G = Goal

. = Empty Path

'#' = Obstacle

---

## Learning Outcomes

* Understanding of search algorithms
* Difference between uninformed and informed search
* Application of adversarial search in games
* Modeling real-world problems using AI techniques

---

## Future Improvements

* Add Alpha-Beta pruning for optimization
* Improve UI for Tic-Tac-Toe
* Add graphical visualization
* Support larger and dynamic mazes

---
