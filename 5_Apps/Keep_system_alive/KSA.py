import time
from pynput.mouse import Controller

# Get the mouse controller instance
mouse = Controller()

# Set the interval in seconds.
# The script will simulate a mouse movement every 60 seconds.
INTERVAL_SECONDS = 60

print("Keeping the system alive. Press Ctrl+C to stop the script.")

try:
    # This infinite loop will keep the script running
    while True:
        # Get the current mouse position
        current_x, current_y = mouse.position
        
        # Simulate a tiny mouse movement (1 pixel to the right and back)
        mouse.move(1, 0)
        mouse.move(-1, 0)
        
        # Print a message to the console for user feedback
        print(f"[{time.strftime('%H:%M:%S')}] Mouse wiggled to prevent lock.")
        
        # Pause the script for the defined interval
        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    # Handle Ctrl+C to stop the script gracefully
    print("\nScript stopped by user. System lock will resume.")
except Exception as e:
    # Catch any other potential errors
    print(f"An error occurred: {e}")
