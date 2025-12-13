"""
NGTube Shorts Usage Example

This example demonstrates how to fetch a random short from YouTube using NGTube.
"""

import sys
import os
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from NGTube import Shorts

def main():
    # Create a Shorts instance
    shorts = Shorts()

    # Fetch a random short
    try:
        short_data = shorts.fetch_short()
        print("Short Data:")
        print(f"Title: {short_data.get('title', 'N/A')}")
        print(f"Video ID: {short_data.get('video_id', 'N/A')}")
        print(f"Channel Name: {short_data.get('channel_name', 'N/A')}")
        print(f"Channel Handle: {short_data.get('channel_handle', 'N/A')}")
        print(f"Channel ID: {short_data.get('channel_id', 'N/A')}")
        print(f"Channel URL: {short_data.get('channel_url', 'N/A')}")
        print(f"Sound Metadata: {short_data.get('sound_metadata', 'N/A')}")
        print(f"Thumbnail: {short_data.get('thumbnail', [])}")
        print(f"Like Count: {short_data.get('like_count', 'N/A')}")
        print(f"View Count: {short_data.get('view_count', 'N/A')}")
        print(f"Comment Count: {short_data.get('comment_count', 'N/A')}")
        print(f"Publish Date: {short_data.get('publish_date', 'N/A')}")
        print(f"Sequence Continuation: {short_data.get('sequence_continuation', 'N/A')}")
        print()

        # Fetch comments for the short
        if short_data.get('video_id'):
            print("Fetching comments...")
            from NGTube import Comments
            comments_obj = Comments(f"https://www.youtube.com/watch?v={short_data['video_id']}")
            comments_data = comments_obj.get_comments(max_comments=50)  # Limit to 50 for demo
            comments = comments_data['comments']
            print(f"Found {len(comments)} comments")
            print()

            # Display first few comments
            for i, comment in enumerate(comments[:5]):  # Show first 5 comments
                print(f"Comment {i+1}:")
                print(f"  Author: {comment['author']}")
                print(f"  Content: {comment['text'][:100]}{'...' if len(comment['text']) > 100 else ''}")
                print(f"  Published: {comment['publishedTimeText']}")
                print(f"  Likes: {comment['likeCount']}")
                print(f"  Replies: {comment['replyCount']}")
                print()

            # Save to JSON
            output_data = {
                "short": short_data,
                "comments": comments
            }
            
            with open("shorts_example.json", "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            
            print("Short data and comments saved to shorts_example.json")
        else:
            print("No comments continuation token found for this short.")
        print()

        # Fetch multiple shorts from feed
        print("Fetching shorts feed...")
        shorts_feed = shorts.fetch_shorts_feed(max_shorts=50)
        print(f"Loaded {len(shorts_feed)} shorts from feed")
        for i, feed_short in enumerate(shorts_feed[:50]):
            print(f"Feed Short {i+1}: {feed_short.get('title', 'N/A')} ({feed_short.get('video_id', 'N/A')})")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()