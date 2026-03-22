"""
PROJECT 1: PERSONAL VOICE ASSISTANT
SyntecxHub - Voice Working for ALL Commands
"""

import datetime
import webbrowser
import os
import random
import win32com.client

# Initialize Windows Voice (ONCE at start)
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    """Speak using Windows built-in TTS - Called for EVERY response"""
    print(f"\n🤖 Assistant: {text}")
    speaker.Speak(text)  # This makes it speak

# ============================================
# COMMAND FUNCTIONS - Each calls speak()
# ============================================

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def tell_day():
    current_day = datetime.datetime.now().strftime("%A")
    speak(f"Today is {current_day}")

def open_notepad():
    speak("Opening Notepad")
    os.system("notepad.exe")

def open_calculator():
    speak("Opening Calculator")
    os.system("calc.exe")

def open_chrome():
    speak("Opening Chrome Browser")
    os.system("start chrome")

def open_paint():
    speak("Opening Paint")
    os.system("mspaint.exe")

def search_google():
    speak("What would you like to search for?")
    query = input("You: ").strip()
    if query:
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("Search cancelled")

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def play_song():
    speak("What song would you like to play?")
    song = input("You: ").strip()
    if song:
        speak(f"Playing {song} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    else:
        speak("Playback cancelled")

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they can't C#!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    speak(random.choice(jokes))

def greet():
    responses = [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Greetings! How may I assist you?"
    ]
    speak(random.choice(responses))

def about_creator():
    speak("I was created by a developer for the SyntecxHub project as a personal voice assistant using Python.")

def show_help():
    speak("Here are the commands you can use.")
    help_text = """
╔══════════════════════════════════════════════════════════════╗
║              📋 VOICE ASSISTANT - COMMANDS LIST              ║
╚══════════════════════════════════════════════════════════════╝

  TIME & DATE:
    time, date, day

  APPLICATIONS:
    notepad, calculator, chrome, paint

  WEB:
    search, youtube, play

  FUN:
    joke, hello, who made you

  HELP:
    help

  EXIT:
    exit, quit
"""
    print(help_text)

# ============================================
# COMMAND PROCESSOR
# ============================================

def process_command(command):
    """Process user command and execute action"""
    
    command = command.lower().strip()
    
    # TIME & DATE
    if command in ["time", "what time is it", "tell me the time"]:
        tell_time()
    
    elif command in ["date", "whats the date", "what is the date"]:
        tell_date()
    
    elif command in ["day", "what day is it", "whats today"]:
        tell_day()
    
    # APPLICATIONS
    elif "notepad" in command:
        open_notepad()
    
    elif "calculator" in command or "calc" in command:
        open_calculator()
    
    elif "chrome" in command:
        open_chrome()
    
    elif "paint" in command:
        open_paint()
    
    # WEB
    elif command == "search":
        search_google()
    
    elif "youtube" in command and "play" not in command:
        open_youtube()
    
    elif command in ["play", "play song", "play music"]:
        play_song()
    
    # FUN
    elif "joke" in command:
        tell_joke()
    
    # GREETINGS
    elif command in ["hello", "hi", "hey"]:
        greet()
    
    # INFORMATION
    elif "who made you" in command or "who created you" in command:
        about_creator()
    
    elif command == "help":
        show_help()
    
    # EXIT
    elif command in ["exit", "quit", "goodbye", "bye"]:
        speak("Goodbye! Have a great day!")
        return False
    
    # UNKNOWN
    else:
        speak("I didn't understand that command. Type 'help' to see what I can do.")
    
    return True

# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """Main program loop"""
    
    # Welcome screen
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🎤 PERSONAL VOICE ASSISTANT - PROJECT 1 🎤               ║
║                                                              ║
║     Voice Working for ALL Responses!                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("✅ Voice Output: WORKING (speaks after every command)")
    print("✅ Input Mode: Keyboard (type your commands)")
    print("\n💡 Type 'help' to see all commands")
    print("💡 Type 'exit' to quit\n")
    print("-" * 55)
    
    # Initial greeting - THIS WILL SPEAK
    speak("Hello! I am your personal voice assistant. Type your commands and I will respond with voice.")
    
    # Main loop
    running = True
    while running:
        try:
            # Get user input
            command = input("\n🎤 You: ").strip()
            
            if command:
                running = process_command(command)
                
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            speak("Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            speak("Sorry, an error occurred. Please try again.")
    
    print("\n" + "="*55)
    print("   👋 Assistant stopped. Thanks for using! 👋")
    print("="*55)

# ============================================
# ENTRY POINT
# ============================================

if __name__ == "__main__":
    main()