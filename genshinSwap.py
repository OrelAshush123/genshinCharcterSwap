print("initialize")
import time
import keyboard as k 
from pynput import mouse
from pynput.mouse import Button
import pyautogui
import threading

SITUATION = None

# List to store the positions of the four clicks
click_positions = []

# Lock to ensure thread-safe operations on click_positions
click_lock = threading.Lock()

def get_pixel_color(x, y):
    """
    Retrieves the RGB color of the pixel at the given (x, y) screen coordinates.
    Returns None if the coordinates are out of the screen bounds.
    """
    screen_width, screen_height = pyautogui.size()
    if x < screen_width and y < screen_height:
        try:
            # pyautogui.pixel returns an (R, G, B) tuple
            return pyautogui.pixel(x, y)
        except Exception as e:
            print(f"Error retrieving pixel at ({x}, {y}): {e}")
            return None
    else:
        return None

def on_click(x, y, button, pressed):
    """
    Callback function that is called on mouse click events.
    Records the position of the click when the mouse button is pressed.
    Stops listening after four clicks.
    """
    if pressed:
        with click_lock:
            if len(click_positions) < 4:
                click_positions.append((x, y))
                print(f"Recorded click {len(click_positions)}: ({x}, {y})")
                print(get_pixel_color(x, y))
                if len(click_positions) == 4:
                    # Stop the listener after four clicks
                    return False

def get_situation(positions):
    global SITUATION
    for idx, (x, y) in enumerate(positions, start=1):
        color = get_pixel_color(x, y)
        avg = sum(color)/3
        if avg < 235: return idx
    print("def:", SITUATION)
    return SITUATION

def monitor_colors(a, b, button, pressed):
    global SITUATION
    try:
        if pressed:
            with click_lock:
                # Make a copy to prevent race conditions
                positions = click_positions.copy()
            if not positions:
                print("No positions to monitor.")
            elif button == Button.x1 or button == Button.x2:
                SITUATION = get_situation(positions)
                if button == Button.x2: SITUATION -= 1
                if button == Button.x1: SITUATION += 1
                if SITUATION == 0: SITUATION = 4
                if SITUATION == 5: SITUATION = 1
                press = str(SITUATION)
                k.press_and_release(str(press))
    except Exception as e:
        print(e)
def main():
    """
    Main function to start the mouse listener and the color monitoring thread.
    """
    # Inform the user to start clicking
    print("Please click 4 times on the screen to record positions.")

    # Start the mouse listener in the main thread
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print("\n4 clicks recorded.")

    # Start the color monitoring in a separate thread
    try:

        listener = mouse.Listener(on_click=monitor_colors)
        listener.start()

        # Keep the main thread alive to allow monitoring
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        listener.stop()
        listener.join()
        print("\nProgram terminated by user.")
        

if __name__ == "__main__":
    main()
