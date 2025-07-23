# 🦴 Lumbar Spine Care Reminder

A beautiful, modern Python GUI application that helps protect your lumbar spine health by providing regular reminders to stand up and stretch.

## ✨ Features

- **🎨 Beautiful GUI Interface** - Modern dark theme with gradient backgrounds and animations
- **⚡ Python-Powered** - Cross-platform Tkinter GUI application  
- **🔊 Smart Notifications** - System sound alerts + auto-close reminders
- **⏱️ Customizable Intervals** - Set reminder frequency from 5-120 minutes  
- **🎯 Health-Focused Design** - Professional health tips and exercise guidance
- **🚀 Easy to Use** - Simple start/stop controls with real-time status updates
- **💾 No Installation Required** - Run directly with Python

## 🖥️ Visual Preview

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    🦴 L U M B A R   S P I N E   C A R E   R E M I N D E R    🦴    ║
║                                                                          ║
║           ✨ Advanced Posture Protection System ✨           ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────── STATUS DISPLAY ─────────────────────┐
│                                                        │
│  Status: ● ACTIVE PROTECTION                     │
│  Interval: 40 minutes                                  │
│  Next Alert: 39:45                              │
│                                                        │
└────────────────────────────────────────────────────────┘
```

## 🛠️ Installation & Running

### Prerequisites

- **Python 3.6+** 
- **Tkinter** (usually comes with Python)

### Quick Start

#### Method 1: Direct Run

```bash
# Clone the repository
git clone https://github.com/yashsharmaskk/posture-correcter-reminder.git
cd posture-correcter-reminder

# Install dependencies (if any)
pip install -r requirements.txt

# Run the application
python lumbar_reminder.py
```

#### Method 2: Create Executable (Optional)

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed lumbar_reminder.py
```

# Build the application
make

# Run the application
make run

# Or run directly
./lumbar_reminder        # Linux/macOS
lumbar_reminder.exe      # Windows
```

#### Method 2: Manual Compilation

**Linux/macOS:**
```bash
g++ -std=c++11 -Wall -O2 -o lumbar_reminder lumbar_reminder.cpp -lpthread
./lumbar_reminder
```

**Windows (MinGW):**
```cmd
g++ -std=c++11 -Wall -O2 -o lumbar_reminder.exe lumbar_reminder.cpp
lumbar_reminder.exe
```

**Windows (MSVC):**
```cmd
cl /EHsc /std:c++11 lumbar_reminder.cpp /Fe:lumbar_reminder.exe
lumbar_reminder.exe
```

### Makefile Commands

| Command | Description |
|---------|-------------|
| `make` or `make all` | Build the application |
| `make run` | Build and run the application |
| `make clean` | Remove build artifacts |
| `make install` | Install to Desktop |
| `make debug` | Build with debug symbols |
| `make help` | Show help information |

## 🚀 Usage

1. **Launch the application** - Run the compiled executable
2. **Start Protection** - Choose option 1 to begin monitoring
3. **Set Interval** - Option 3 to customize reminder frequency
4. **View Status** - Real-time display of protection status
5. **Get Health Tips** - Option 5 for spine care guidance

### Menu Options

- **🚀 Start Protection** - Activate spine monitoring
- **⛔ Stop Protection** - Deactivate monitoring
- **⏱️ Set Reminder Interval** - Customize timing (5-120 minutes)
- **📊 View Status** - Check current protection status
- **❓ Health Tips** - Professional spine care advice
- **🚪 Exit Application** - Close the program

## 🎯 Reminder Features

When it's time for a break, you'll see:

- **🚨 Spectacular Alert Screen** - Impossible to miss visual alerts
- **🔊 Audio Notifications** - System beep sounds
- **💻 System Notifications** - Native OS notifications
- **📋 Action Checklist** - Clear instructions for spine care

## 🎨 Technical Features

### Cross-Platform Compatibility
- **Windows**: Uses Windows API for beep sounds and console colors
- **macOS**: Uses osascript for notifications
- **Linux**: Uses notify-send for desktop notifications

### Performance Optimizations
- **Multithreaded Design** - Separate threads for UI and reminders
- **Low CPU Usage** - Efficient timer management
- **Memory Efficient** - Minimal resource consumption

### Visual Enhancements
- **ANSI Color Support** - Rich terminal colors
- **Unicode Emoji Support** - Modern visual elements
- **Box Drawing Characters** - Professional interface design
- **Real-time Updates** - Dynamic countdown displays

## 🏥 Health Benefits

Regular use of this application can help:
- **Reduce Lower Back Pain** - Prevention through movement
- **Improve Posture** - Regular posture checks
- **Increase Productivity** - Better focus through breaks
- **Prevent Long-term Issues** - Proactive spine care

## 🔧 Customization

The application supports:
- **Flexible Timing** - 5 to 120 minute intervals
- **Personalized Messages** - Modify reminder text in source
- **Color Themes** - Adjust ANSI colors in code
- **Sound Settings** - Customize notification sounds

## 🐛 Troubleshooting

### Common Issues

**Colors not showing on Windows:**
- Enable Virtual Terminal Processing in Windows Terminal
- Use Windows Terminal or PowerShell instead of Command Prompt

**Notifications not working:**
- **Linux**: Install `libnotify-bin` (`sudo apt install libnotify-bin`)
- **macOS**: Notifications should work by default
- **Windows**: PowerShell must be available

**Compilation errors:**
- Ensure C++11 or later compiler
- Check that all required headers are available
- Use appropriate compiler flags for your platform

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to submit issues, suggestions, or improvements!

## 💙 Health Disclaimer

This application is a reminder tool. Always consult with healthcare professionals for serious back pain or spinal issues.

---

**Take care of your spine - it's the only one you have! 🦴💪**
