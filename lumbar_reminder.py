"""
🦴 Lumbar Spine Care Reminder Application

A beautiful GUI application that helps protect your back health by reminding
you to stand up and stretch at regular intervals. Perfect for people who
spend long hours sitting at a desk.

Features:
- Customizable reminder intervals (5-120 minutes)
- Beautiful dark theme with animations
- Sound notifications
- Snooze functionality
- Health tips and exercise guidance
- Auto-close reminders

Author: Created with care for your spine health 💙
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from datetime import datetime, timedelta
import os
import math

class LumbarReminderApp:
    """
    Main application class for the Lumbar Spine Care Reminder.
    
    This class creates a beautiful GUI that helps users maintain good spine health
    by providing regular reminders to stand up, stretch, and move around.
    """
    
    def __init__(self, root):
        """
        Initialize the application with all necessary settings and UI components.
        
        Args:
            root: The main Tkinter window
        """
        # === WINDOW SETUP === 
        self.root = root
        self.root.title("🦴 Lumbar Spine Care Reminder")
        self.root.geometry("600x550")  # Perfect size for all elements
        self.root.configure(bg='#0f0f23')  # Dark space-like background
        self.root.resizable(False, False)  # Keep window size fixed for best appearance
        
        # Try to set a custom icon (optional)
        try:
            self.root.iconbitmap(default='')
        except:
            pass  # No worries if icon doesn't work
        
        # === ANIMATION VARIABLES ===
        # These create smooth pulsing effects for the UI
        self.pulse_alpha = 0
        self.pulse_direction = 1
        self.gradient_offset = 0
        
        # === USER SETTINGS ===
        self.reminder_interval = tk.IntVar(value=40)  # How often to remind (minutes)
        self.is_running = False  # Is the reminder system active?
        self.reminder_thread = None  # Background thread for timing
        self.next_reminder_time = None  # When is the next reminder due?
        
        # === START THE APP ===
        self.setup_ui()  # Create the beautiful interface
        self.update_clock()  # Start the real-time clock
        self.animate_ui()  # Start the smooth animations
        
    def setup_ui(self):
        """
        Create the beautiful user interface with gradient backgrounds,
        modern controls, and a professional health-focused design.
        """
        
        # === MAIN CANVAS FOR GRAPHICS ===
        # This allows us to create gradients and custom visual effects
        self.canvas = tk.Canvas(
            self.root,
            width=600,
            height=550,
            bg='#0f0f23',
            highlightthickness=0  # Remove ugly border
        )
        self.canvas.pack(fill='both', expand=True)
        
        # Create the beautiful gradient background
        self.create_gradient_background()
        
        # === APP TITLE SECTION ===
        # Create a stunning title with shadow effect
        self.title_frame = tk.Frame(self.canvas, bg='#0f0f23')
        self.canvas.create_window(300, 80, window=self.title_frame)
        
        # Shadow effect (darker text behind)
        title_shadow = tk.Label(
            self.title_frame,
            text="🦴 LUMBAR SPINE CARE",
            font=("Impact", 28, "bold"),
            fg='#1a1a2e',  # Dark shadow color
            bg='#0f0f23'
        )
        title_shadow.pack()
        
        # Main title (bright text on top)
        title_main = tk.Label(
            self.title_frame,
            text="🦴 LUMBAR SPINE CARE",
            font=("Impact", 28, "bold"),
            fg='#00d4ff',  # Bright cyan color
            bg='#0f0f23'
        )
        title_main.place(in_=title_shadow, x=-2, y=-2)  # Offset for shadow effect
        
        # === SUBTITLE ===
        # Professional tagline
        subtitle = tk.Label(
            self.canvas,
            text="✨ Advanced Posture Protection System ✨",
            font=("Consolas", 14, "italic"),
            fg='#ff6b9d',  # Pink accent color
            bg='#0f0f23'
        )
        self.canvas.create_window(300, 120, window=subtitle)
        
        # === CONTROL PANEL ===
        # This is where users adjust their settings
        self.control_panel = tk.Frame(
            self.canvas,
            bg='#16213e',  # Darker blue background
            relief='flat',
            bd=0,
            padx=30,
            pady=25
        )
        self.canvas.create_window(300, 220, window=self.control_panel)
        
        # Add a glowing border around the control panel
        self.canvas.create_rectangle(
            170, 170, 430, 270,
            outline='#00d4ff',  # Cyan glow
            width=2,
            fill='',
            tags='glow_border'
        )
        
        # === TIME SETTING CONTROLS ===
        # Label for the time slider
        time_label = tk.Label(
            self.control_panel,
            text="⏱️ REMINDER INTERVAL",
            font=("Arial Black", 12),
            fg='#ffffff',
            bg='#16213e'
        )
        time_label.pack(pady=(5, 10))
        
        # Container for the slider
        slider_frame = tk.Frame(self.control_panel, bg='#16213e')
        slider_frame.pack(pady=5)
        
        # The main time adjustment slider (5-120 minutes)
        self.time_slider = tk.Scale(
            slider_frame,
            from_=5,  # Minimum 5 minutes
            to=120,   # Maximum 2 hours
            variable=self.reminder_interval,
            orient=tk.HORIZONTAL,  # Horizontal slider
            font=("Arial", 11, "bold"),
            fg='#00d4ff',          # Cyan text
            bg='#0f0f23',          # Dark background
            activebackground='#ff6b9d',  # Pink when dragging
            highlightbackground='#16213e',
            troughcolor='#1a1a2e', # Slider track color
            length=250,            # Width of slider
            width=20,              # Height of slider
            sliderlength=30        # Size of the handle
        )
        self.time_slider.pack()
        
        # Display showing current time setting
        self.time_display = tk.Label(
            self.control_panel,
            text="40 minutes",
            font=("Consolas", 12, "bold"),
            fg='#ff6b9d',
            bg='#16213e'
        )
        self.time_display.pack(pady=(5, 10))
        
        # Connect slider to update function
        self.time_slider.config(command=self.update_time_display)
        
        # === MAIN CONTROL BUTTONS ===
        # Container for start/stop buttons
        button_panel = tk.Frame(self.canvas, bg='#0f0f23')
        self.canvas.create_window(300, 320, window=button_panel)
        
        # START button - begins spine protection monitoring
        self.start_button = tk.Button(
            button_panel,
            text="🚀 START PROTECTION",
            font=("Arial Black", 12),
            bg='#00ff88',          # Bright green = GO!
            fg='#0f0f23',          # Dark text on bright background
            activebackground='#00cc6a',  # Darker green when pressed
            activeforeground='#0f0f23',
            command=self.start_reminders,  # What happens when clicked
            width=18,
            height=2,
            relief='flat',         # Modern flat design
            bd=0,                  # No ugly border
            cursor='hand2'         # Show pointer cursor on hover
        )
        self.start_button.pack(side=tk.LEFT, padx=15)
        
        # STOP button - stops the monitoring (disabled by default)
        self.stop_button = tk.Button(
            button_panel,
            text="⛔ STOP PROTECTION",
            font=("Arial Black", 12),
            bg='#ff4757',          # Red = STOP!
            fg='white',
            activebackground='#ff3742',
            activeforeground='white',
            command=self.stop_reminders,   # What happens when clicked
            width=18,
            height=2,
            state=tk.DISABLED,     # Can't stop if not started
            relief='flat',
            bd=0,
            cursor='hand2'
        )
        self.stop_button.pack(side=tk.LEFT, padx=15)
        
        # === STATUS DISPLAY SECTION ===
        # Shows current system status and countdown
        self.status_panel = tk.Frame(
            self.canvas,
            bg='#1a1a2e',         # Dark blue-gray background
            relief='flat',
            bd=0,
            padx=25,
            pady=20
        )
        self.canvas.create_window(300, 420, window=self.status_panel)
        
        # Glowing border around status display
        self.canvas.create_rectangle(
            150, 380, 450, 460,
            outline='#ff6b9d',    # Pink glow
            width=2,
            fill='',
            tags='status_glow'
        )
        
        # Current status indicator (STANDBY, ACTIVE, etc.)
        self.status_indicator = tk.Label(
            self.status_panel,
            text="● STANDBY",
            font=("Consolas", 14, "bold"),
            fg='#ffa502',         # Orange for standby
            bg='#1a1a2e'
        )
        self.status_indicator.pack()
        
        # Countdown display (time until next reminder)
        self.countdown_display = tk.Label(
            self.status_panel,
            text="Ready to protect your spine",
            font=("Consolas", 12),
            fg='#95a5a6',         # Light gray
            bg='#1a1a2e'
        )
        self.countdown_display.pack(pady=(5, 0))
        
        # === FOOTER MESSAGE ===
        # Encouraging message at the bottom
        footer = tk.Label(
            self.canvas,
            text="💙 Your health is our priority 💙",
            font=("Arial", 10, "italic"),
            fg='#6c5ce7',         # Purple accent
            bg='#0f0f23'
        )
        self.canvas.create_window(300, 510, window=footer)
        
    def create_gradient_background(self):
        """
        Create a smooth color gradient from dark blue to lighter blue.
        This gives our app a professional, modern look that's easy on the eyes.
        """
        # Draw 550 horizontal lines, each with a slightly different color
        for i in range(550):
            # Color values for our gradient (RGB format)
            dark_blue = (15, 15, 35)     # Very dark blue at top
            medium_blue = (26, 33, 62)   # Medium blue in middle  
            accent_blue = (16, 33, 62)   # Slightly different blue at bottom
            
            # Calculate where we are in the gradient (0.0 to 1.0)
            ratio = i / 550
            
            # Blend colors smoothly
            if ratio < 0.5:  # First half of gradient
                factor = ratio * 2
                r = int(dark_blue[0] + (medium_blue[0] - dark_blue[0]) * factor)
                g = int(dark_blue[1] + (medium_blue[1] - dark_blue[1]) * factor)
                b = int(dark_blue[2] + (medium_blue[2] - dark_blue[2]) * factor)
            else:  # Second half of gradient  
                factor = (ratio - 0.5) * 2
                r = int(medium_blue[0] + (accent_blue[0] - medium_blue[0]) * factor)
                g = int(medium_blue[1] + (accent_blue[1] - medium_blue[1]) * factor)
                b = int(medium_blue[2] + (accent_blue[2] - medium_blue[2]) * factor)
            
            # Convert to hex color format and draw the line
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, 600, i, fill=color, tags='gradient')
    
    def animate_ui(self):
        """
        Create subtle pulsing animations to make the interface feel alive.
        This runs continuously in the background to create smooth effects.
        """
        # Create a pulsing effect (like breathing)
        self.pulse_alpha += self.pulse_direction * 0.1
        
        # Reverse direction when we reach the limits
        if self.pulse_alpha >= 1:
            self.pulse_alpha = 1
            self.pulse_direction = -1  # Start fading out
        elif self.pulse_alpha <= 0.3:
            self.pulse_alpha = 0.3
            self.pulse_direction = 1   # Start fading in
            
        # Update visual effects (could be enhanced in the future)
        if hasattr(self, 'canvas'):
            # Rotate gradient offset for future animations
            self.gradient_offset = (self.gradient_offset + 1) % 360
            
        # Schedule the next animation frame (10 times per second)
        self.root.after(100, self.animate_ui)
    
    def start_reminders(self):
        """
        Start the spine protection system!
        This begins monitoring and will show reminders at the set interval.
        """
        # Only start if we're not already running
        if not self.is_running:
            # Update our status
            self.is_running = True
            
            # Update button states and colors
            self.start_button.config(state=tk.DISABLED, bg='#2d3436')  # Disabled gray
            self.stop_button.config(state=tk.NORMAL, bg='#ff4757')     # Active red
            self.time_slider.config(state=tk.DISABLED)  # Can't change while running
            
            # Calculate when the first reminder should appear
            self.next_reminder_time = datetime.now() + timedelta(minutes=self.reminder_interval.get())
            self.update_status()  # Refresh the display
            
            # Start the background monitoring thread
            self.reminder_thread = threading.Thread(target=self.reminder_loop, daemon=True)
            self.reminder_thread.start()
            
    def stop_reminders(self):
        """
        Stop the spine protection system.
        This turns off monitoring and resets everything back to standby mode.
        """
        # Turn off the monitoring
        self.is_running = False
        
        # Reset button states and colors
        self.start_button.config(state=tk.NORMAL, bg='#00ff88')     # Active green
        self.stop_button.config(state=tk.DISABLED, bg='#2d3436')   # Disabled gray
        self.time_slider.config(state=tk.NORMAL)  # Can change settings again
        
        # Clear the next reminder time and update display
        self.next_reminder_time = None
        self.update_status()
        
    def reminder_loop(self):
        """
        This runs in the background and checks every minute if it's time
        to show a reminder. This is the "heart" of our monitoring system.
        """
        # Keep checking as long as the system is running
        while self.is_running:
            time.sleep(60)  # Wait 1 minute between checks
            
            # Is it time for a reminder?
            if self.is_running and datetime.now() >= self.next_reminder_time:
                self.show_reminder()  # Show the dramatic reminder popup!
                
                # Schedule the next reminder (if still running)
                if self.is_running:
                    self.next_reminder_time = datetime.now() + timedelta(minutes=self.reminder_interval.get())
                    
    def show_reminder(self):
        """
        THE BIG MOMENT! Show a spectacular, impossible-to-ignore reminder window
        that will definitely get the user's attention and motivate them to move.
        
        This creates a dramatic, colorful popup with health instructions and
        convenient action buttons.
        """
        # Play attention-getting sound first
        self.play_notification_sound()
        
        # === CREATE THE REMINDER WINDOW ===
        reminder_window = tk.Toplevel(self.root)
        reminder_window.title("🦴 Spine Protection Alert")
        reminder_window.geometry("500x400")  # Nice size for readability
        reminder_window.configure(bg='#0f0f23')
        reminder_window.attributes('-topmost', True)  # Always on top!
        reminder_window.resizable(False, False)
        
        # Center the window on screen for maximum impact
        screen_width = reminder_window.winfo_screenwidth()
        screen_height = reminder_window.winfo_screenheight()
        x = (screen_width / 2) - 250   # Center horizontally  
        y = (screen_height / 2) - 200  # Center vertically
        reminder_window.geometry(f"+{int(x)}+{int(y)}")
        
        # === CREATE DRAMATIC BACKGROUND ===
        canvas = tk.Canvas(
            reminder_window,
            width=500,
            height=400,
            bg='#0f0f23',
            highlightthickness=0
        )
        canvas.pack(fill='both', expand=True)
        
        # Create eye-catching gradient (red to orange to purple to dark)
        for i in range(400):
            ratio = i / 400
            
            if ratio < 0.3:
                # Red to orange section (urgent feel)
                factor = ratio / 0.3
                r = int(255 - (255 - 220) * factor)  # Red to orange
                g = int(71 + (140 - 71) * factor)
                b = int(87 + (0 - 87) * factor)
            elif ratio < 0.7:
                # Orange to purple section (transition)
                factor = (ratio - 0.3) / 0.4
                r = int(220 - (220 - 156) * factor)  # Orange to purple
                g = int(140 - (140 - 39) * factor)
                b = int(0 + (176 - 0) * factor)
            else:
                # Purple to dark section (fade to bottom)
                factor = (ratio - 0.7) / 0.3
                r = int(156 - (156 - 15) * factor)   # Purple to dark
                g = int(39 - (39 - 15) * factor)
                b = int(176 - (176 - 35) * factor)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(0, i, 500, i, fill=color)
        
        # === ADD GLOWING BORDER EFFECT ===
        # Multiple rectangles create a glowing effect
        for i in range(5):
            canvas.create_rectangle(
                i, i, 500-i, 400-i,
                outline='#00d4ff',  # Bright cyan glow
                width=1,
                fill=''
            )
        
        # === WARNING ICON ===
        # Big attention-getting warning symbol
        alert_frame = tk.Frame(canvas, bg='#ff4757')  # Red background
        canvas.create_window(250, 80, window=alert_frame)
        
        alert_icon = tk.Label(
            alert_frame,
            text="⚠️",              # Warning emoji
            font=("Arial", 48),     # Really big!
            bg='#ff4757',
            fg='#ffffff'
        )
        alert_icon.pack(padx=20, pady=10)
        
        # === MAIN ALERT MESSAGE ===
        main_message = tk.Label(
            canvas,
            text="🚨 SPINE PROTECTION ALERT 🚨",
            font=("Impact", 22, "bold"),
            fg='#ffffff',           # White text
            bg='#ff4757'            # Red background
        )
        canvas.create_window(250, 150, window=main_message)
        
        # === URGENT CALL TO ACTION ===
        urgent_msg = tk.Label(
            canvas,
            text="TIME TO STAND UP!",
            font=("Arial Black", 18),
            fg='#ffff00',           # Bright yellow
            bg='#0f0f23'
        )
        canvas.create_window(250, 190, window=urgent_msg)
        
        # === HEALTH INSTRUCTION PANEL ===
        # Professional-looking panel with specific health guidance
        instructions = tk.Frame(canvas, bg='#1a1a2e', padx=20, pady=15)
        canvas.create_window(250, 260, window=instructions)
        
        # Header for instructions
        inst_title = tk.Label(
            instructions,
            text="🎯 IMMEDIATE ACTIONS REQUIRED:",
            font=("Consolas", 12, "bold"),
            fg='#00ff88',           # Bright green
            bg='#1a1a2e'
        )
        inst_title.pack(pady=(0, 10))
        
        # List of specific actions to take (evidence-based health advice)
        health_actions = [
            "🚶 Stand up and walk for 2-3 minutes",     # Movement
            "🤸 Perform gentle back stretches",          # Flexibility  
            "💆 Roll your shoulders backwards",          # Posture reset
            "🧘 Take 3 deep breaths and relax"          # Stress relief
        ]
        
        # Display each action with clear formatting
        for action in health_actions:
            action_label = tk.Label(
                instructions,
                text=action,
                font=("Consolas", 11),
                fg='#ffffff',
                bg='#1a1a2e',
                anchor='w'              # Left-align text
            )
            action_label.pack(anchor='w', pady=2)
        
        # === ACTION BUTTONS ===
        # Give users clear options for what to do next
        button_frame = tk.Frame(canvas, bg='#0f0f23')
        canvas.create_window(250, 350, window=button_frame)
        
        # DONE button - for when they've completed their break
        done_button = tk.Button(
            button_frame,
            text="✅ DONE - THANKS!",
            font=("Arial Black", 14),
            bg='#00ff88',           # Success green
            fg='#0f0f23',
            activebackground='#00cc6a',
            command=reminder_window.destroy,  # Close the window
            width=15,
            height=2,
            relief='flat',
            bd=0,
            cursor='hand2'
        )
        done_button.pack(side=tk.LEFT, padx=10)
        
        # SNOOZE button - for when they need a few more minutes
        snooze_button = tk.Button(
            button_frame,
            text="😴 SNOOZE 5 MIN",
            font=("Arial Black", 12),
            bg='#ff6b9d',           # Pink color
            fg='white',
            activebackground='#e55a87',
            command=lambda: self.snooze_reminder(reminder_window),  # 5-minute delay
            width=15,
            height=2,
            relief='flat',
            bd=0,
            cursor='hand2'
        )
        snooze_button.pack(side=tk.LEFT, padx=10)
        
        # === AUTO-CLOSE COUNTDOWN ===
        # Automatically close after 30 seconds if no action taken
        self.auto_close_countdown = 30
        self.countdown_label = tk.Label(
            canvas,
            text=f"Auto-close in {self.auto_close_countdown}s",
            font=("Consolas", 10),
            fg='#95a5a6',           # Light gray
            bg='#0f0f23'
        )
        canvas.create_window(250, 380, window=self.countdown_label)
        
        # Start the countdown timer and pulsing effects
        self.update_countdown(reminder_window)
        self.pulse_reminder_window(reminder_window, canvas)
    
    def snooze_reminder(self, window):
        """
        User chose to snooze - give them 5 more minutes before the next reminder.
        This is helpful when they're in the middle of something important.
        """
        window.destroy()  # Close the current reminder
        
        if self.is_running:
            # Set next reminder for 5 minutes from now (instead of full interval)
            self.next_reminder_time = datetime.now() + timedelta(minutes=5)
    
    def update_countdown(self, window):
        """
        Update the auto-close countdown every second.
        This ensures the reminder doesn't stay open forever if ignored.
        """
        # Check if the countdown label still exists (window might be closed)
        if hasattr(self, 'countdown_label') and self.countdown_label.winfo_exists():
            if self.auto_close_countdown > 0:
                # Update the countdown display
                self.countdown_label.config(text=f"Auto-close in {self.auto_close_countdown}s")
                self.auto_close_countdown -= 1
                
                # Schedule next update in 1 second
                window.after(1000, lambda: self.update_countdown(window))
            else:
                # Time's up! Close the window automatically
                window.destroy()
    
    def pulse_reminder_window(self, window, canvas):
        """
        Add a pulsing rainbow effect to the reminder window border.
        This creates an eye-catching animation that's impossible to ignore.
        """
        try:
            if window.winfo_exists():
                # Cycle through different colors for the pulsing border
                rainbow_colors = ['#00d4ff', '#ff6b9d', '#00ff88', '#ffff00']
                current_color = rainbow_colors[int(time.time() * 2) % len(rainbow_colors)]

                # Remove previous pulse borders to prevent stacking rectangles
                canvas.delete('pulse_border')

                # Update all border rectangles with the current color
                for i in range(5):
                    canvas.create_rectangle(
                        i, i, 500-i, 400-i,
                        outline=current_color,
                        width=1,
                        fill='',
                        tags='pulse_border'  # Tag for easy updating
                    )

                # Schedule next color change in 0.5 seconds
                window.after(500, lambda: self.pulse_reminder_window(window, canvas))
        except Exception:
            # If window is closed or error occurs, just stop the animation
            pass

    def update_clock(self):
        """
        Update the real-time display elements.
        This method is called periodically to keep the interface current.
        """
        # Update the status display if running
        if self.is_running:
            self.update_status()
        
        # Schedule next update in 1 second
        self.root.after(1000, self.update_clock)
    
    def update_time_display(self, value=None):
        """
        Update the time display when the user changes the slider.
        Shows the current reminder interval in a user-friendly format.
        """
        minutes = self.reminder_interval.get()
        
        if minutes == 1:
            text = "1 minute"
        elif minutes < 60:
            text = f"{minutes} minutes"
        elif minutes == 60:
            text = "1 hour"
        else:
            hours = minutes // 60
            remaining_minutes = minutes % 60
            if remaining_minutes == 0:
                text = f"{hours} hours"
            else:
                text = f"{hours}h {remaining_minutes}m"
        
        self.time_display.config(text=text)
    
    def update_status(self):
        """
        Update the status display with current system information.
        Shows whether the system is running and when the next reminder is due.
        """
        if self.is_running:
            # System is active - show countdown to next reminder
            self.status_indicator.config(
                text="● ACTIVE",
                fg='#00ff88'  # Bright green for active
            )
            
            if self.next_reminder_time:
                # Calculate time remaining until next reminder
                time_remaining = self.next_reminder_time - datetime.now()
                
                if time_remaining.total_seconds() > 0:
                    minutes_left = int(time_remaining.total_seconds() / 60)
                    seconds_left = int(time_remaining.total_seconds() % 60)
                    
                    if minutes_left > 0:
                        countdown_text = f"Next reminder in {minutes_left}m {seconds_left}s"
                    else:
                        countdown_text = f"Next reminder in {seconds_left}s"
                else:
                    countdown_text = "Reminder due now!"
                
                self.countdown_display.config(text=countdown_text)
        else:
            # System is on standby
            self.status_indicator.config(
                text="● STANDBY",
                fg='#ffa502'  # Orange for standby
            )
            self.countdown_display.config(text="Ready to protect your spine")
    
    def play_notification_sound(self):
        """
        Play a notification sound to get the user's attention.
        Uses Windows system beep - works on most systems without additional dependencies.
        """
        try:
            import winsound
            # Play a series of beeps for attention
            for _ in range(3):
                winsound.Beep(800, 200)  # 800Hz for 200ms
                time.sleep(0.1)
        except ImportError:
            # Fallback for non-Windows systems
            try:
                import os
                os.system('echo \a')  # Terminal bell sound
            except:
                pass  # Silent if no sound available


def main():
    """
    Main function to start the Lumbar Spine Care Reminder application.
    Creates the main window and starts the GUI event loop.
    """
    # Create the main application window
    root = tk.Tk()
    
    # Create and start the application
    app = LumbarReminderApp(root)
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
