# OAuth 2.0 Setup Guide for X API

## Overview

This guide walks you through setting up OAuth 2.0 authentication for the X API to enable the daily posting workflow. This is a one-time setup process that will generate the necessary tokens for the automated workflow.

## Prerequisites

- Access to your X Developer Portal
- A web browser (on your Windows host system)
- Your Client ID and Client Secret

## Step 1: Configure X Developer Portal

1. Log in to the [X Developer Portal](https://developer.x.com)
2. Navigate to your project/app settings
3. Under "User authentication settings":
   - Ensure "OAuth 2.0" is enabled
   - Add the following scopes: `tweet.read`, `tweet.write`, `offline.access`
4. Under "App info":
   - Add `https://localhost/` as a Callback URI / Redirect URL
   - Save your changes

## Step 2: Generate OAuth 2.0 Tokens

### Option A: Using the Authorization URL

1. Copy this URL and open it in your browser:
```
https://twitter.com/i/oauth2/authorize?response_type=code&client_id=YUZFNTJjYXFLWVlhMnc0bnZvbzI6MTpjaQ&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=tweet.read+tweet.write+offline.access&state=EGOS&code_challenge=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&code_challenge_method=S256
```

2. Log in to X.com if needed and authorize the application
3. You'll be redirected to a URL like:
```
https://localhost/?code=AUTHORIZATION_CODE&state=EGOS
```
4. Copy the entire URL - you'll need it in the next step

### Option B: Using a Python Script on Windows

If you have Python installed on your Windows machine, you can run this script:

```python
import webbrowser
import requests
import base64
import json
import os

# Your app credentials
CLIENT_ID = "YUZFNTJjYXFLWVlhMnc0bnZvbzI6MTpjaQ"
CLIENT_SECRET = "6SnueKQ27p_YvefU70f6Oxfo91oHkB-pHfNQhsbI1u3HmYfCgW"
REDIRECT_URI = "https://localhost/"

# Step 1: Open authorization URL
auth_url = f"https://twitter.com/i/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=tweet.read+tweet.write+offline.access&state=EGOS&code_challenge=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&code_challenge_method=S256"
print(f"Opening browser to: {auth_url}")
webbrowser.open(auth_url)

# Step 2: Get the authorization code from the redirect URL
redirect_url = input("After authorizing, paste the full redirect URL here: ")
code = redirect_url.split("code=")[1].split("&")[0]

# Step 3: Exchange the code for tokens
token_url = "https://api.twitter.com/2/oauth2/token"
auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "code": code,
    "grant_type": "authorization_code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "code_verifier": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
}

response = requests.post(token_url, headers=headers, data=data)
tokens = response.json()

print("\n✅ SUCCESS! Add these to GitHub Secrets:")
print("\nX_OAUTH2_ACCESS_TOKEN:")
print(tokens["access_token"])
print("\nX_OAUTH2_REFRESH_TOKEN:")
print(tokens["refresh_token"])

# Save to a file for reference
with open("oauth2_tokens.txt", "w") as f:
    f.write(f"X_OAUTH2_ACCESS_TOKEN={tokens['access_token']}\n")
    f.write(f"X_OAUTH2_REFRESH_TOKEN={tokens['refresh_token']}\n")

print("\nTokens also saved to oauth2_tokens.txt")
```

## Step 3: Exchange the Authorization Code for Tokens

If you used Option A above, you need to exchange the authorization code for tokens:

1. Open a terminal on your Windows machine
2. Run the following curl command (replace YOUR_AUTH_CODE with the code from the URL):

```bash
curl -X POST "https://api.twitter.com/2/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic $(echo -n 'YUZFNTJjYXFLWVlhMnc0bnZvbzI6MTpjaQ:6SnueKQ27p_YvefU70f6Oxfo91oHkB-pHfNQhsbI1u3HmYfCgW' | base64)" \
  -d "code=YOUR_AUTH_CODE&grant_type=authorization_code&client_id=YUZFNTJjYXFLWVlhMnc0bnZvbzI6MTpjaQ&redirect_uri=https://localhost/&code_verifier=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```

3. The response will contain your access_token and refresh_token

## Step 4: Add Tokens to GitHub Secrets

1. Go to your GitHub repository: https://github.com/enioxt/EGOSystem
2. Navigate to Settings → Secrets and variables → Actions
3. Add two new repository secrets:
   - `X_OAUTH2_ACCESS_TOKEN`: The access token you received
   - `X_OAUTH2_REFRESH_TOKEN`: The refresh token you received

## Step 5: Test the Workflow

1. Go to the Actions tab in your GitHub repository
2. Select the "X Daily Post" workflow
3. Click "Run workflow"
4. Provide an optional summary and keyword
5. Click "Run workflow" to start the job

## Troubleshooting

- If you get a 403 Forbidden error, ensure your app has the correct permissions in the X Developer Portal
- If tokens expire, you may need to regenerate them using this process
- Check the workflow logs for detailed error messages

## References

- [X API OAuth 2.0 Documentation](https://developer.x.com/docs/authentication/oauth2)
- [GitHub Actions Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- Related files:
  - [Daily Post Workflow](/.github/workflows/x_daily_post.yml)
  - [Post to X Script](/scripts/utils/post_to_x.py)