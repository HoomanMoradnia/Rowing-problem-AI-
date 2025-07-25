# Rowing Problem AI

A Python-based AI project that visualizes and solves the "rowing problem"—a path-finding challenge on a river grid filled with obstacles—using multiple classic search algorithms. The project features an interactive Pygame GUI where users can explore how BFS, DFS, and A* algorithms perform in real time.

## Features

- **Interactive Visualization:** Watch pathfinding algorithms (BFS, DFS, A*) step through a grid representing a river with obstacles.
- **Algorithm Selection:** Choose which algorithm to visualize, or generate a random river matrix with obstacles.
- **Performance Metrics:** Displays the energy used (steps in the path) and the number of explored nodes for each algorithm.
- **Custom River Maps:** Supports loading river layouts from a JSON file (e.g., `sample.json`).
- **Animated Boat Movement:** Animates a boat image moving along the discovered path.
- **Randomized Challenge:** Option to generate a random obstacle map for increased difficulty and algorithm comparison.

## How It Works

- The river is represented as a 2D grid loaded from `sample.json` (or generated randomly).
- Obstacles are shown in black, water in cyan, and the optimal path in yellow/orange.
- The user selects an algorithm (BFS, DFS, A*) or opts to generate a new random grid.
- The selected algorithm finds a path from the top-left to the bottom-right of the grid, animating the process.
- The display updates with metrics about the search's efficiency.

## Requirements

- Python 3.x
- Pygame

## Installation

### Windows

1. **Install Python:**  
   Download and install Python 3.x from [python.org](https://www.python.org/downloads/windows/).  
   Make sure to check the box "Add Python to PATH" during installation.

2. **Clone the repository:**  
   Open Command Prompt and run:
   ```bash
   git clone https://github.com/HoomanMoradnia/Rowing-problem-AI-.git
   cd Rowing-problem-AI-
   ```

3. **Install Pygame:**  
   ```bash
   pip install pygame
   ```

4. **Verify additional files:**  
   Ensure you have `sample.json` (river grid) and `Boat.jpg` (boat image) in the project directory.

5. **Run the application:**  
   ```bash
   python AI.py
   ```

### Linux

1. **Install Python:**  
   Most Linux distributions come with Python pre-installed. To ensure you have Python 3.x, run:
   ```bash
   python3 --version
   ```

   If Python 3 is not installed, install it (for Ubuntu/Debian):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Clone the repository:**  
   ```bash
   git clone https://github.com/HoomanMoradnia/Rowing-problem-AI-.git
   cd Rowing-problem-AI-
   ```

3. **Install Pygame:**  
   ```bash
   pip3 install pygame
   ```

4. **Verify additional files:**  
   Ensure you have `sample.json` (river grid) and `Boat.jpg` (boat image) in the project directory.

5. **Run the application:**  
   ```bash
   python3 AI.py
   ```

## Usage

- **Menu:** Select BFS, A*, DFS, or generate a random matrix.
- **Visuals:** The grid, obstacles, and animated solution path will appear in the window.
- **Metrics:** Energy used and node exploration stats are displayed on screen.

## File Structure

- `AI.py` — Main application and all algorithm logic.
- `sample.json` — Example river grid (required for running the app).
- `Boat.jpg` — Image used to animate the boat (required).
- `LICENSE` — MIT License.

## Algorithms

- **BFS (Breadth-First Search):** Explores neighbors level by level to find the shortest path.
- **DFS (Depth-First Search):** Explores as far as possible along each branch before backtracking.
- **A* Search:** Uses heuristics (Manhattan distance) for efficient, optimal pathfinding.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

- Developed by Hooman Moradnia.
- Pygame for visualization.

---
*Enjoy visualizing and comparing classic AI pathfinding algorithms on the rowing problem!*
