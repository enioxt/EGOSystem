#!/usr/bin/env python3
# @references(level=0):
# - .windsurfrules
# - CODE_OF_CONDUCT.md
# - MQP.md
# - ROADMAP.md
# - CROSSREF_STANDARD.md
# - scripts/utils/post_to_x.py

"""
OAuth 2.0 Token Generator for X API

This script performs the OAuth 2.0 PKCE flow to obtain access and refresh tokens
for the X API. These tokens are required for the post_to_x.py script to use
the modern v2 API endpoints.

The script will:
1. Open a browser window to authorize the application
2. Ask you to paste the redirect URL
3. Extract and display the OAuth 2.0 tokens

After running, add the tokens to your GitHub repository secrets:
- X_OAUTH2_ACCESS_TOKEN
- X_OAUTH2_REFRESH_TOKEN

These will be used automatically by post_to_x.py when available.
"""

import os
import sys
import webbrowser
from pathlib import Path

try:
    import tweepy
except ImportError:
    print("Installing tweepy...")
    os.system(f"{sys.executable} -m pip install tweepy")
    import tweepy

# Configuration
CLIENT_ID = "YUZFNTJjYXFLWVlhMnc0bnZvbzI6MTpjaQ"
CLIENT_SECRET = "6SnueKQ27p_YvefU70f6Oxfo91oHkB-pHfNQhsbI1u3HmYfCgW"
REDIRECT_URI = "https://localhost/"
SCOPES = ["tweet.read", "tweet.write", "offline.access"]

def main():
    print("\n=== X API OAuth 2.0 Token Generator ===")
    print("This script will help you generate the OAuth 2.0 tokens needed for post_to_x.py")
    
    # Initialize the OAuth 2.0 handler
    auth = tweepy.OAuth2UserHandler(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,  # Optional for PKCE
        redirect_uri=REDIRECT_URI,
        scope=SCOPES
    )
    
    # Get the authorization URL
    try:
        auth_url = auth.get_authorization_url()
    except Exception as e:
        sys.exit(f"Error generating authorization URL: {e}")
    
    print("\n1. Opening browser to authorize the application...")
    print(f"Authorization URL: {auth_url}")
    print("\n2. Log in to X.com if needed and authorize the application")
    print("3. You'll be redirected to a URL starting with 'https://localhost/?...'")
    print("4. Copy the ENTIRE redirected URL and paste it below")
    
    # Don't try to open browser in WSL - just provide the URL
    print(f"\n📋 COPY THIS URL and open it in your Windows browser:\n{auth_url}")
    print("\nNOTE: Since we're in WSL, you'll need to manually copy/paste this URL to your browser.")
    print("After authorizing, you'll be redirected to a URL starting with 'https://localhost/?...'")
    print("Copy that entire URL and paste it back here.")
    
    # Get the redirect response from user input
    redirect_response = input("\nPaste the full redirect URL here: ")
    
    # Exchange the authorization code for tokens
    try:
        tokens = auth.fetch_token(redirect_response)
        
        print("\n✅ SUCCESS! Add these to GitHub Secrets:")
        print("\nX_OAUTH2_ACCESS_TOKEN:")
        print(tokens["access_token"])
        
        refresh_token = tokens.get("refresh_token")
        if refresh_token:
            print("\nX_OAUTH2_REFRESH_TOKEN:")
            print(refresh_token)
        else:
            print("\n⚠️ No refresh token returned. The access token will expire in ~2 hours.")
            print("Make sure 'offline.access' scope is enabled in your X Developer Portal.")
        
        # Save tokens to a local file for reference
        token_file = Path(__file__).parent / "oauth2_tokens.txt"
        with open(token_file, "w") as f:
            f.write(f"X_OAUTH2_ACCESS_TOKEN={tokens['access_token']}\n")
            if refresh_token:
                f.write(f"X_OAUTH2_REFRESH_TOKEN={refresh_token}\n")
        
        print(f"\nTokens also saved to {token_file} for reference")
        print("\nAdd these tokens to your GitHub repository secrets:")
        print("1. Go to https://github.com/enioxt/EGOSystem/settings/secrets/actions")
        print("2. Click 'New repository secret'")
        print("3. Add the two secrets with the exact names shown above")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()