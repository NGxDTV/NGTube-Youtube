"""
NGTube Search Usage Example

This example demonstrates how to use the Search class to perform YouTube searches
and extract video results.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from NGTube import Search
import json

def main():
    # Example search query
    query = "Python programming tutorials"

    # Create a Search instance with a maximum of 200 results
    search = Search(query, max_results=200)

    # Perform the search
    print(f"Searching for: {query}")
    search.perform_search()

    # Get the results
    results = search.get_results()

    # Print summary
    print(f"Estimated total results: {results['estimated_results']}")
    print(f"Loaded videos: {results['loaded_videos']}")
    print("\nFirst 5 video results:")

    # Print first 5 videos
    for i, video in enumerate(results['videos'][:5], 1):
        print(f"\n{i}. {video['title']}")
        print(f"   Channel: {video['channel']}")
        print(f"   Views: {video['viewCount']}")
        print(f"   Duration: {video['length']}")
        print(f"   Published: {video['publishedTime']}")
        print(f"   Video ID: {video['videoId']}")
        print(f"   URL: https://www.youtube.com/watch?v={video['videoId']}")

    # Save results to a JSON file
    with open("search_example_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"\nFull results saved to search_example_results.json")

if __name__ == "__main__":
    main()