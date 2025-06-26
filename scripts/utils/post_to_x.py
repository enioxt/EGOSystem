# @references(level=0):
# - .windsurfrules
# - CODE_OF_CONDUCT.md
# - MQP.md
# - ROADMAP.md
# - CROSSREF_STANDARD.md

#!/usr/bin/env python3
"""Post a summary tweet to X/Twitter.

Environment variables required (store as GitHub secrets!):
    X_API_KEY
    X_API_SECRET
    X_ACCESS_TOKEN
    X_ACCESS_SECRET

Usage: python post_to_x.py --text "Hello world" [--reply-to 123456]
If --text is omitted the script will attempt to load the latest daily summary
from reports/daily/<latest>/tweet.txt.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import tweepy  # type: ignore

REPO_ROOT = Path(__file__).resolve().parents[2]
DAILY_DIR = REPO_ROOT / "reports" / "daily"


def find_latest_tweet_text() -> str | None:
    if not DAILY_DIR.exists():
        return None
    latest = max(DAILY_DIR.glob("*/tweet.txt"), default=None, key=lambda p: p.parent.name)
    if latest and latest.is_file():
        return latest.read_text().strip()
    return None


def create_client() -> tweepy.Client:
    key = os.getenv("X_API_KEY")
    secret = os.getenv("X_API_SECRET")
    token = os.getenv("X_ACCESS_TOKEN")
    token_secret = os.getenv("X_ACCESS_SECRET")
    if not all([key, secret, token, token_secret]):
        sys.exit("Missing X API credentials in environment variables. Aborting.")
    return tweepy.Client(
        consumer_key=key,
        consumer_secret=secret,
        access_token=token,
        access_token_secret=token_secret,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="Tweet text (<=280 chars)")
    parser.add_argument("--reply-to", help="Tweet ID to reply to", default=None)
    args = parser.parse_args()

    text = args.text or find_latest_tweet_text()
    if not text:
        sys.exit("No tweet text provided and could not find default tweet.txt")
    if len(text) > 280:
        sys.exit(f"Tweet too long ({len(text)} chars). Trim to 280 or less.")

    client = create_client()
    resp = client.create_tweet(text=text, in_reply_to_tweet_id=args.reply_to)
    tweet_url = f"https://x.com/user/status/{resp.data['id']}"  # replace 'user' with handle if known
    print(f"Tweet posted: {tweet_url}")


if __name__ == "__main__":
    main()