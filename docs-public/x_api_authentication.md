# X API Authentication Guide

## Overview

This document explains the authentication methods used for the automated daily posting workflow to X.com (formerly Twitter).

## Authentication Methods

The EGOS system supports two authentication methods for X API:

1. **OAuth 1.0a (Legacy)** - Uses consumer keys and access tokens
2. **OAuth 2.0 (Modern)** - Uses client ID/secret and user access tokens with scopes

Our implementation in `scripts/utils/post_to_x.py` supports both methods, with OAuth 2.0 preferred when available.

## Required Credentials

### OAuth 1.0a Credentials
- `X_API_KEY` - Consumer API Key
- `X_API_SECRET` - Consumer API Secret
- `X_ACCESS_TOKEN` - User Access Token
- `X_ACCESS_SECRET` - User Access Secret

### OAuth 2.0 Credentials
- `X_CLIENT_ID` - OAuth 2.0 Client ID
- `X_CLIENT_SECRET` - OAuth 2.0 Client Secret
- `X_OAUTH2_ACCESS_TOKEN` - OAuth 2.0 User Access Token
- `X_OAUTH2_REFRESH_TOKEN` - OAuth 2.0 Refresh Token

## Setting Up OAuth 2.0

To set up OAuth 2.0 authentication:

1. Configure your app in the X Developer Portal:
   - Enable OAuth 2.0 with scopes: `tweet.read`, `tweet.write`, `offline.access`
   - Add a callback URL: `https://localhost/`

2. Run the token generator script:
   ```bash
   python scripts/utils/get_oauth2_tokens.py
   ```

3. Add the generated tokens to GitHub repository secrets.

## Troubleshooting

If you encounter a 403 Forbidden error with message "Your client app is not configured with the appropriate oauth1 app permissions for this endpoint", it means:

1. You're using OAuth 1.0a tokens with a v2 endpoint that requires OAuth 2.0
2. You need to generate OAuth 2.0 tokens using the process above

## References

- [X API Documentation](https://developer.x.com/docs)
- [Tweepy Documentation](https://docs.tweepy.org/)
- Related files:
  - [Daily Post Workflow](/.github/workflows/x_daily_post.yml)
  - [Post to X Script](/scripts/utils/post_to_x.py)
  - [OAuth 2.0 Token Generator](/scripts/utils/get_oauth2_tokens.py)