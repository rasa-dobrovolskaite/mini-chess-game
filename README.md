# Project: ♟️ A Chess Question ♟️

#### <p>A Chess Question is a Python program that aims to show which black figure a white figure can capture, based on a board setup entered by the user, with one white figure and up to 16 black figures.</p>

---

### <p>Getting Started ✅ :

To install the project, follow these steps:

1. Clone the repository

2. Navigate to project root directory via terminal

3. Initiate .venv environment:

``` python3 -m venv .venv ``` <br><br>
``` source ./.venv/bin/activate ```

4. Install needed packages using requirements.txt:

``` pip install -r requirements.txt ``` </p>

---

### <p> Usage 💻 :

1. To start the program, run:

``` python main.py ```

2. Now the program will display an empty chess board and ask for the user input to enter a white piece.

3. Once white piece is entered correctly, the program will display the board with added piece and will ask the user to enter black pieces (up to 16 pieces).

4. Every time a piece is added the program confirms if piece is added successfully or not and will display the updated board.

5. Once user enters all pieces, the program will print out the final board which highlights in red all the black pieces, if there are any, that white piece can capture.

Note: As chess figure symbols are displayed using Unicode characters, the display of the figures can vary depending on your terminal theme colors (For example, dark themes may show black pieces as white). To have the most accurate display, using light theme is recommended. </p>
