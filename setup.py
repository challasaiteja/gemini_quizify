#!/usr/bin/env python3
"""
Setup script for Gemini Quizify
This script helps you configure the application for your Google Cloud project
"""

import os
import subprocess
import sys

def check_gcloud_installed():
    """Check if gcloud CLI is installed"""
    try:
        result = subprocess.run(['gcloud', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def check_gcloud_auth():
    """Check if user is authenticated with gcloud"""
    try:
        result = subprocess.run(['gcloud', 'auth', 'list', '--filter=status:ACTIVE'], 
                              capture_output=True, text=True)
        return 'ACTIVE' in result.stdout
    except:
        return False

def setup_gcloud_auth():
    """Set up gcloud authentication"""
    print("🔐 Setting up Google Cloud authentication...")
    
    if not check_gcloud_installed():
        print("❌ Google Cloud CLI is not installed.")
        print("Please install it from: https://cloud.google.com/sdk/docs/install")
        return False
    
    if check_gcloud_auth():
        print("✅ Already authenticated with Google Cloud")
        return True
    
    print("Running: gcloud auth application-default login")
    try:
        subprocess.run(['gcloud', 'auth', 'application-default', 'login', 
                       '--scopes=https://www.googleapis.com/auth/cloud-platform'], 
                      check=True)
        print("✅ Successfully authenticated with Google Cloud")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to authenticate with Google Cloud")
        return False

def get_project_id():
    """Get the current Google Cloud project ID"""
    try:
        result = subprocess.run(['gcloud', 'config', 'get-value', 'project'], 
                              capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except:
        pass
    return None

def update_config_file(project_id):
    """Update the config.py file with the project ID"""
    if not project_id:
        print("⚠️  No project ID found. Please set it manually in config.py")
        return False
    
    # Read current config
    with open('config.py', 'r') as f:
        content = f.read()
    
    # Replace the placeholder
    updated_content = content.replace('"your-project-id-here"', f'"{project_id}"')
    
    # Write back
    with open('config.py', 'w') as f:
        f.write(updated_content)
    
    print(f"✅ Updated config.py with project ID: {project_id}")
    return True

def main():
    """Main setup function"""
    print("🚀 Gemini Quizify - Setup")
    print("=" * 50)
    
    # Step 1: Set up gcloud authentication
    print("\n1. Setting up Google Cloud authentication...")
    if not setup_gcloud_auth():
        print("❌ Please fix authentication issues before continuing")
        return False
    
    # Step 2: Get project ID
    print("\n2. Getting Google Cloud project ID...")
    project_id = get_project_id()
    if project_id:
        print(f"✅ Found project: {project_id}")
    else:
        print("⚠️  No project ID found. Please set one with: gcloud config set project YOUR_PROJECT_ID")
        project_id = input("Enter your Google Cloud project ID: ").strip()
        if not project_id:
            print("❌ No project ID provided")
            return False
    
    # Step 3: Update config file
    print("\n3. Updating configuration...")
    update_config_file(project_id)
    
    # Step 4: Final validation
    print("\n4. Final validation...")
    from config import validate_config
    issues = validate_config()
    if issues:
        print("❌ Configuration issues found:")
        for issue in issues:
            print(f"   - {issue}")
    else:
        print("✅ Configuration is ready!")
        print("\n🎉 You can now run the application with: python run_app.py")
    
    return len(issues) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
