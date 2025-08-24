import customtkinter as ctk
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import threading
import sys
import ctypes
import os

class App(ctk.CTk):
    """
    The main CustomTkinter application class.
    
    This class now encapsulates the GUI, input listeners, and the system
    locking logic, making the code more modular and self-contained.
    """
    def __init__(self):
        super().__init__()
        
        # Configure the main window
        self.title("PC Lock on Input")
        self.geometry("300x150")
        self.resizable(False, False)
        
        # Configure the grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create the status label
        self.status_label = ctk.CTkLabel(self, text="Ready to monitor.", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, padx=20, pady=10)

        # Create the monitoring button
        self.start_button = ctk.CTkButton(self, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Listeners will be stored as instance attributes
        self.keyboard_listener = None
        self.mouse_listener = None

        # A flag to prevent multiple lock calls
        self.is_locking = False

    def _lock_and_exit(self):
        """
        Locks the Windows system and then terminates the script.
        
        This private method handles the core logic of locking the system
        and exiting the application. It's called by the input listeners.
        """
        if self.is_locking:
            return
        
        self.is_locking = True
        
        # Stop the listeners to ensure a clean exit
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        if self.mouse_listener:
            self.mouse_listener.stop()

        # Check if the operating system is Windows to ensure the lock function works.
        if os.name == 'nt':
            try:
                # Call the LockWorkStation function from user32.dll
                ctypes.windll.user32.LockWorkStation()
                print("System locked successfully. Exiting...")
            except Exception as e:
                print(f"Error locking the system: {e}")
            
        # Exit the application cleanly after the action.
        sys.exit()

    def _on_press(self, key):
        """
        Callback for keyboard key presses.
        """
        print("Key pressed. Locking system...")
        self._lock_and_exit()

    def _on_move(self, x, y):
        """
        Callback for mouse movement.
        """
        print("Mouse moved. Locking system...")
        self._lock_and_exit()
        # Returning False stops the mouse listener
        return False

    def start_monitoring(self):
        """
        Starts the input listeners in separate threads.
        
        This public method is the entry point for starting the monitoring
        process from the GUI.
        """
        self.status_label.configure(text="Monitoring active... Move mouse or press a key to lock.")
        self.start_button.configure(state="disabled") # Disable button to prevent multiple starts

        # Create a non-blocking keyboard listener and start it
        self.keyboard_listener = KeyboardListener(on_press=self._on_press)
        self.keyboard_listener_thread = threading.Thread(target=self.keyboard_listener.start)
        self.keyboard_listener_thread.daemon = True
        self.keyboard_listener_thread.start()

        # Create a non-blocking mouse listener and start it
        self.mouse_listener = MouseListener(on_move=self._on_move)
        self.mouse_listener_thread = threading.Thread(target=self.mouse_listener.start)
        self.mouse_listener_thread.daemon = True
        self.mouse_listener_thread.start()

        print("Monitoring started. The script will now listen for input.")

if __name__ == "__main__":
    app = App()
    app.mainloop()

