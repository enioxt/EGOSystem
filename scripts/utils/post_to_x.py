# @references(level=0):
# - .windsurfrules
# - CODE_OF_CONDUCT.md
# - MQP.md
# - ROADMAP.md
# - CROSSREF_STANDARD.md

#!/usr/bin/env python3
"""Post automated daily summary and report link to X/Twitter.

Environment variables required (store as GitHub secrets!):
    X_API_KEY
    X_API_SECRET
    X_ACCESS_TOKEN
    X_ACCESS_SECRET

The script publishes two tweets as a thread:
1. Summary tweet: `<summary> #EEAS $ETHIK #EGOS #<KEYWORD>`
2. Reply tweet with the link to the full report on GitHub: `Full report: <report_url> #EEAS $ETHIK #EGOS #<KEYWORD>`

Usage example:
    python -m scripts.utils.post_to_x \
        --summary "Build succeeded" \
        --keyword DAILY \
        --report-url "https://github.com/enioxt/EGOSystem/actions/runs/12345"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import requests
from requests_oauthlib import OAuth1

# Mantenha tweepy como fallback se necessário
try:
    import tweepy  # type: ignore
    TWEEPY_AVAILABLE = True
except ImportError:
    TWEEPY_AVAILABLE = False

REPO_ROOT = Path(__file__).resolve().parents[2]
DAILY_DIR = REPO_ROOT / "reports" / "daily"


def find_latest_tweet_text() -> str | None:
    if not DAILY_DIR.exists():
        return None
    latest = max(DAILY_DIR.glob("*/tweet.txt"), default=None, key=lambda p: p.parent.name)
    if latest and latest.is_file():
        return latest.read_text().strip()
    return None


def get_oauth1_auth():
    # OAuth 1.0a credentials
    key = os.getenv("X_API_KEY")
    secret = os.getenv("X_API_SECRET")
    token = os.getenv("X_ACCESS_TOKEN")
    token_secret = os.getenv("X_ACCESS_SECRET")
    
    if not all([key, secret, token, token_secret]):
        sys.exit("Missing X API credentials in environment variables. Aborting.")
    
    print("Using OAuth 1.0a authentication with API v2 endpoints")
    print(f"API Key: {key[:5]}...")
    print(f"Access Token: {token[:5]}...")
    
    return OAuth1(key, secret, token, token_secret)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", help="Summary text (<=280 chars)")
    parser.add_argument("--keyword", help="Additional hashtag without #, will be converted to UPPERCASE", default="DAILY")
    parser.add_argument("--report-url", help="URL to the full report", required=True)
    args = parser.parse_args()

    summary = args.summary or find_latest_tweet_text() or "Daily project update."
    keyword = args.keyword.upper()
    report_url = args.report_url

    hashtags = f"#EEAS $ETHIK #EGOS #{keyword}"

    # Build summary tweet and ensure 280 char limit
    max_summary_len = 280 - len(hashtags) - 1  # space
    summary = summary.strip()
    if len(summary) > max_summary_len:
        summary = summary[: max_summary_len - 3].rstrip() + "..."
    summary_tweet = f"{summary} {hashtags}"

    report_tweet = f"Full report: {report_url} {hashtags}"
    if len(report_tweet) > 280:
        # hashtags and link may already occupy many chars; truncate if needed
        excess = len(report_tweet) - 280
        report_tweet = report_tweet[:-excess - 3] + "..."

    auth = get_oauth1_auth()
    url = "https://api.twitter.com/2/tweets"
    
    try:
        # Post first tweet using API v2 with OAuth 1.0a
        print(f"Posting summary tweet: {summary_tweet[:30]}...")
        payload = {"text": summary_tweet}
        response = requests.post(url, json=payload, auth=auth)
        
        # Check response and get tweet ID
        if response.status_code != 201:
            print(f"Error posting summary tweet. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            sys.exit(1)
            
        response_data = response.json()
        first_id = response_data["data"]["id"]
        print(f"Summary posted with API v2. ID: {first_id}")
        
        # Post reply tweet
        print(f"Posting report tweet: {report_tweet[:30]}...")
        reply_payload = {
            "text": report_tweet,
            "reply": {"in_reply_to_tweet_id": first_id}
        }
        
        reply_response = requests.post(url, json=reply_payload, auth=auth)
        
        # Check response
        if reply_response.status_code != 201:
            print(f"Error posting reply tweet. Status code: {reply_response.status_code}")
            print(f"Response: {reply_response.text}")
            sys.exit(1)
            
        reply_data = reply_response.json()
        reply_id = reply_data["data"]["id"]
        print(f"Report link posted with API v2. ID: {reply_id}")
        
        print("✅ Posts completed successfully!")
        print(f"View at: https://x.com/i/status/{first_id}")

    except Exception as e:
        print(f"Error posting to X: {e}")
        print("Response details (if available):")
        try:
            if 'response' in locals() and hasattr(response, 'text'):
                print(response.text)
        except:
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()