"""
Configuration file for Gemini Quizify
Update these values with your Google Cloud project details
"""

import os

# Google Cloud Configuration
# Replace these with your actual project details
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id-here")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")

# Model Configuration
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "textembedding-gecko@003")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-pro")

# Embedding Configuration
EMBED_CONFIG = {
    "model_name": EMBEDDING_MODEL,
    "project": GOOGLE_CLOUD_PROJECT,
    "location": GOOGLE_CLOUD_LOCATION
}

# LLM Configuration
LLM_CONFIG = {
    "model_name": LLM_MODEL,
    "temperature": 0.8,
    "max_output_tokens": 500
}

def validate_config():
    """Validate that required configuration is present"""
    issues = []
    
    if not GOOGLE_CLOUD_PROJECT or GOOGLE_CLOUD_PROJECT == "your-project-id-here":
        issues.append("Google Cloud Project ID not configured")
    
    return issues

def print_config_status():
    """Print current configuration status"""
    print("🔧 Configuration Status:")
    print(f"  Project ID: {GOOGLE_CLOUD_PROJECT}")
    print(f"  Location: {GOOGLE_CLOUD_LOCATION}")
    print(f"  Embedding Model: {EMBEDDING_MODEL}")
    print(f"  LLM Model: {LLM_MODEL}")
    
    issues = validate_config()
    if issues:
        print("\n⚠️  Configuration Issues:")
        for issue in issues:
            print(f"  - {issue}")
        print("\n📝 Please update config.py with your project details")
    else:
        print("\n✅ Configuration looks good!")
