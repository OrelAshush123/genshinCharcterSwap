# README.txt for Genshin Impact Character Swap Script

##Description

This script will help you swap characters in **Genshin Impact** using the side buttons on your mouse. The Python script takes four mouse clicks to record the positions of the characters' avatars on the screen. Once the positions are set, you can use the mouse side buttons (`x1` or `x2`) to swap between characters in the game.

## How It Works

1. **Recording Character Positions:**
   - The script will prompt you to click four times on the screen to mark the positions of your characters' avatars in the game.
   
2. **Character Swapping:**
   - After recording the character positions, pressing the side mouse buttons will automatically swap characters:
     - `x1` button: Cycles to the next character.
     - `x2` button: Cycles to the previous character.

   The script will send a key press (`1`, `2`, `3`, or `4`) to the game to switch to the appropriate character.

## Prerequisites

Ensure you have the following Python libraries installed:

- `keyboard`: For simulating key presses.
- `pynput`: For detecting mouse events.
- `pyautogui`: For identifying pixel colors (used in case you want to add color-based logic for character health bars, etc.).

You can install these libraries with:

```bash
pip install keyboard pynput pyautogui
```

## Usage Instructions

1. **Run the Script:**
   - Open a terminal and run the script with Python:
     ```bash
     python script_name.py
     ```

2. **Click to Set Character Positions:**
   - The script will prompt you to click four times on the character avatars in Genshin Impact to set their screen positions.

3. **Swap Characters Using Side Buttons:**
   - Use the `x1` button to switch to the next character and the `x2` button to switch to the previous character. The game will recognize this as pressing the corresponding number keys (`1`, `2`, `3`, `4`).

## Notes

- The script simulates key presses (`1`, `2`, `3`, or `4`), so ensure these are the default character swap keys in **Genshin Impact**.
- You need a mouse with side buttons (`x1` and `x2`) to use this script.

## Termination

To stop the program, press `Ctrl+C` in the terminal or close the script window.

[![Watch the video](https://img.youtube.com/vi/eAGYL5vfUgo/maxresdefault.jpg)](https://www.youtube.com/watch?v=eAGYL5vfUgo)

