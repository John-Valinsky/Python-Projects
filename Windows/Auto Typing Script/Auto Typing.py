import pyautogui
import time
import keyboard  # Import keyboard module
from datetime import datetime  # Import datetime for time tracking

# Set a maximum typing speed in seconds (lower means faster)
MIN_TYPING_DELAY = 0.05  # Minimum delay (in seconds) between keystrokes

def type_line_by_line(filepath, typing_delay):
    """Simulates typing effect by sending keystrokes from a file with a delay, and exits on ESC key."""
    try:
        start_time = datetime.now()  # Record start time
        # Format the start time as Time Day Month Year
        print(f"Start time: {start_time.strftime('%H:%M:%S %d %b %Y')}")

        with open(filepath, 'r') as file:
            print("File opened successfully.")
            while True:
                if keyboard.is_pressed('esc'):
                    print("ESC pressed. Exiting typing.")
                    break

                ch = file.read(1)  # Read one character at a time
                if not ch:  # End of file
                    print("Reached end of file.")
                    break
                pyautogui.write(ch)  # Simulate typing each character
                time.sleep(typing_delay)  # Add typing delay between characters

        end_time = datetime.now()  # Record end time
        # Format the end time as Time Day Month Year
        print(f"End time: {end_time.strftime('%H:%M:%S %d %b %Y')}")

        # Calculate and display duration without milliseconds
        duration = end_time - start_time
        total_seconds = duration.total_seconds()
        formatted_duration = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
        print(f"Operation completed in: {formatted_duration} (H:M:S)")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("\n")
    text_art = """
  ████████╗██╗  ██╗███████╗    ██╗    ██╗██████╗ ██╗████████╗███████╗██████╗ 
  ╚══██╔══╝██║  ██║██╔════╝    ██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
     ██║   ███████║█████╗      ██║ █╗ ██║██████╔╝██║   ██║   █████╗  ██████╔╝
     ██║   ██╔══██║██╔══╝      ██║███╗██║██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗
     ██║   ██║  ██║███████╗    ╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
     ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                           
    """
    print(text_art)

    print("---------------------------------------------------------------------------------")
    print("                           ~ ~  By John Valinsky  ~ ~ ")
    print("---------------------------------------------------------------------------------")

    # Prompt the user for the file path
    filename = input("Enter the path to the text file: ")

    # Ask the user for the typing speed
    typing_speed = input("Enter the typing speed in seconds (minimum 0.05 seconds): ")
    try:
        typing_delay = float(typing_speed)
        if typing_delay < MIN_TYPING_DELAY:
            print(f"Speed too fast! Setting typing speed to minimum of {MIN_TYPING_DELAY} seconds.")
            typing_delay = MIN_TYPING_DELAY
    except ValueError:
        print("Invalid input! Setting typing speed to minimum of 0.1 seconds.")
        typing_delay = 0.1  # Default typing speed

    # Ask the user for the delay before starting to type
    cursor_delay = input("Enter the delay time in seconds to set the cursor position: ")
    try:
        cursor_delay = float(cursor_delay)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return  # Exit the program if input is invalid

    # Let the user know to set the cursor
    print(f"\nYou have {cursor_delay} seconds to place the cursor where the text will be written.")
    time.sleep(cursor_delay)  # Wait for user-defined seconds before typing starts

    print(f"\nReading from file: {filename}\n")

    # Call the function to simulate typing
    type_line_by_line(filename, typing_delay)

    # Wait for user to press ENTER before exiting
    input("Press Enter to exit...")  # Keeps the console open until Enter is pressed


if __name__ == "__main__":
    main()
