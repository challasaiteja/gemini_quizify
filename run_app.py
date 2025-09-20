#!/usr/bin/env python3
"""
Main application runner for Gemini Quizify
Run this script to start the complete quiz application
"""

import subprocess
import sys
import os

def main():
    """Run the main application"""
    try:
        # Check if we're in the right directory
        if not os.path.exists('task_10.py'):
            print("Error: Please run this script from the project root directory")
            sys.exit(1)
        
        print("Starting Gemini Quizify Application...")
        print("Make sure you have:")
        print("1. Installed all requirements: pip install -r requirements.txt")
        print("2. Set up Google Cloud credentials")
        print("3. Configured the project ID in the embed_config")
        print("\nStarting Streamlit app...")
        
        # Run the main application
        subprocess.run([sys.executable, "-m", "streamlit", "run", "task_10.py"], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error running application: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
