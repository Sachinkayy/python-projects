# Python Projects (Mini Games & CLI Practice)

A curated set of beginner-to-intermediate **Python CLI projects** that focus on core programming fundamentals:  
**input handling, loops, conditionals, randomness, strings, game logic, and basic OOP**.

This repository is built as a “learn-by-building” collection—each project is small, runnable, and designed to strengthen a specific set of concepts.

---

## What’s Inside

### Project Index

| # | Project | Type | Key Concepts | How to Run |
|---|--------|------|--------------|------------|
| 1 | **Mad Libs** (`p1madlibs.py`) | CLI | strings, `f-strings`, user input | `python p1madlibs.py` |
| 2 | **Guess the Number** (`p2_guess_the_number.py`) | CLI | loops, `random`, comparisons | `python p2_guess_the_number.py` |
| 3 | **Rock Paper Scissors (Basic)** (`p3-rock-ppr-scissor.py`) | CLI | game loop, randomness, win logic | `python p3-rock-ppr-scissor.py` |
| 4 | **Hangman** (`P4-HANGMAN/`) | CLI | sets, validation, word list, loops | `python P4-HANGMAN/P4-hangman.py` |
| 5 | **Quiz Game** (`P5-quiz-game/`) | CLI | dictionaries, random questions, scoring | `python P5-quiz-game/p5-quiz-game.py` |
| 6 | **Tic Tac Toe vs Computer** (`p6-tic-tac-toe/`) | CLI | board logic, validation, win checks | `python p6-tic-tac-toe/p6-tic-tac-toe.py` |
| 7 | **Rock Paper Scissors (OOP)** (`p7-rock-paper-scissor-using-oops.py`) | CLI | classes, state, structured gameplay | `python p7-rock-paper-scissor-using-oops.py` |

---

## Highlights (Why this repo is worth a look)

### Solid fundamentals, not just “toy scripts”
These projects intentionally practice real programming skills:
- **Input validation** (e.g., Tic Tac Toe bounds checking)
- **Game state management** (turns, board, lives, score)
- **Reusable logic** (win conditions, helper functions)
- **Data structures**: lists, sets, dictionaries

### Multiple versions of the same idea (great for growth)
Rock–Paper–Scissors appears twice:
- A **basic functional** version
- An **OOP version** showing progression to cleaner structure

---

## Getting Started

### Requirements
- **Python 3.x**
- No external dependencies (pure Python)

### Clone the repo
```bash
git clone https://github.com/Sachinkayy/python-projects.git
cd python-projects
```

### Run any project
```bash
python <filename.py>
```

Example:
```bash
python p2_guess_the_number.py
```

---

## Project Details

## 1) Mad Libs — `p1madlibs.py`
A fun “fill in the blanks” generator using user input + formatted strings.

**Concepts used**
- `input()`
- `f-strings`
- basic string composition

---

## 2) Guess the Number — `p2_guess_the_number.py`
The computer selects a random number and you keep guessing until you match.

**Concepts used**
- `random.randint()`
- `while` loop
- comparison-based hints (too high / too low)

---

## 3) Rock Paper Scissors (Basic) — `p3-rock-ppr-scissor.py`
Classic RPS in the terminal, including a quit option.

**Concepts used**
- randomness + repeated rounds
- win-check helper function
- user decision loop

---

## 4) Hangman — `P4-HANGMAN/`
A complete Hangman implementation with a large word bank.

**Files**
- `P4-HANGMAN/P4-hangman.py` — main game logic
- `P4-HANGMAN/words.py` — word list

**Concepts used**
- `set()` operations for guessed letters and remaining letters
- filtering invalid words (no hyphens/spaces)
- lives system and game-over states

Run:
```bash
python P4-HANGMAN/P4-hangman.py
```

---

## 5) Quiz Game — `P5-quiz-game/`
Randomized short quiz using a dictionary of questions → answers.

**Concepts used**
- dictionary-based question bank
- random selection of questions
- scoring + replay flow

Run:
```bash
python P5-quiz-game/p5-quiz-game.py
```

---

## 6) Tic Tac Toe vs Computer — `p6-tic-tac-toe/`
Playable Tic Tac Toe against a computer that chooses random available moves.

**Concepts used**
- 2D board representation
- mapping positions (`position_dict`)
- input validation (`isnumeric`, bounds checking, occupied slot checking)
- win checks: rows, columns, diagonals

Run:
```bash
python p6-tic-tac-toe/p6-tic-tac-toe.py
```

---

## 7) Rock Paper Scissors (OOP) — `p7-rock-paper-scissor-using-oops.py`
A class-based version of RPS with cleaner organization and a simple game loop.

**Concepts used**
- class structure (`Game`)
- encapsulated gameplay
- stateful player name + repeated rounds

Run:
```bash
python p7-rock-paper-scissor-using-oops.py
```

---

## Author
**Sachin Kayy**  
GitHub: https://github.com/Sachinkayy

If you found these projects helpful or fun, consider starring the repo!
