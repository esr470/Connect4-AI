# 🎮 Connect 4 AI

A Connect 4 game implemented in **Python** using **Pygame**, **NumPy**, and the **Minimax algorithm**.

The project includes an additional **GUI visualization of the Minimax decision tree** as a bonus feature.

---

## ✨ Features

* 🎮 Interactive Connect 4 game
* 🤖 AI opponent using the **Minimax algorithm**
* 🧠 AI searches up to a specified depth
* 🌳 Visual representation of the Minimax tree
* 📊 Displays the values of tree nodes
* 🖥️ Separate window for the AI decision tree
* ⚡ Uses NumPy for board representation and calculations

---

## 🧠 AI Algorithm

The AI uses the **Minimax algorithm** to select its moves.

The algorithm explores possible future moves and evaluates the board using a simple heuristic based on the number of AI pieces on the board.

The current search depth is:

```text
Depth = 4
```

---

## 🎨 GUI

The game interface is built using **Pygame**.

A bonus visualization window displays the Minimax tree, including:

* 🌳 Tree nodes
* 🔗 Connections between nodes
* 🔢 Node values
* 🟣 Maximizing nodes
* 🟠 Minimizing nodes

---

## 🛠️ Technologies Used

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| Python     | Main programming language             |
| Pygame     | Game interface and visualization      |
| NumPy      | Board representation and calculations |
| Minimax    | AI decision-making                    |

---

## 📁 Project Structure

```text
Connect4-AI/
│
├── connect4_ai.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Connect4-AI.git
```

### 2. Open the project folder

```bash
cd Connect4-AI
```

### 3. Install the required libraries

```bash
pip install pygame numpy
```

### 4. Run the game

```bash
python connect4_ai.py
```

---

## 🎮 How to Play

1. Run the program.
2. The player uses the mouse to select a column.
3. The player's piece is placed in the selected column.
4. The AI calculates its move using Minimax.
5. The AI places its piece automatically.
6. The Minimax tree visualization appears in a separate window.

---

## 🧩 Main Components

### Board

The game uses a **6 × 7** Connect 4 board.

```text
Rows    = 6
Columns = 7
```

### Player

The human player is represented by:

```text
PLAYER = 1
```

### AI

The AI is represented by:

```text
AI = 2
```

### Minimax

The `minimax()` function explores possible moves and selects the best move for the AI.

### Tree Visualization

The project includes a bonus GUI that displays the generated Minimax tree and its evaluated values.

---

## 🚀 Future Improvements

Possible improvements include:

* 🏆 Detecting wins and draws
* 🧠 More advanced heuristic evaluation
* ✂️ Alpha-Beta pruning
* 🎚️ Adjustable AI difficulty
* 🎨 Improved game interface
* 📈 More detailed AI statistics

---
