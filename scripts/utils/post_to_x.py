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

    client = create_client()

    # Post summary tweet
    first = client.create_tweet(text=summary_tweet)
    first_id = first.data["id"]
    print(f"Summary posted. ID: {first_id}")

    # Post reply with report link
    reply = client.create_tweet(text=report_tweet, in_reply_to_tweet_id=first_id)
    print(f"Report link posted. ID: {reply.data['id']}")


if __name__ == "__main__":
    main()