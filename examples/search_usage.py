"""
NGTube Search Usage Example

This example demonstrates how to use the Search class to perform YouTube searches
and extract video results with various filters.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from NGTube import Search, SearchFilters
import json

def main():
    # Example 1: Basic search
    print("=== Basic Search ===")
    search_basic = Search("Python programming", max_results=10)
    search_basic.perform_search()
    results_basic = search_basic.get_results()
    print(f"Query: {results_basic['query']}")
    print(f"Estimated results: {results_basic['estimated_results']}")
    print(f"Loaded items: {results_basic['loaded_items']}")
    videos = [item for item in results_basic['items'] if item['type'] == 'video']
    print(f"Videos: {len(videos)}")
    print()

    # Example 2: Search with filter for channels only
    print("=== Search Channels Only ===")
    search_channels = Search("Python programming", max_results=10, filter=SearchFilters.CHANNELS)
    search_channels.perform_search()
    results_channels = search_channels.get_results()
    print(f"Query: {results_channels['query']}")
    print(f"Filter: {results_channels['filter']} (Channels only)")
    print(f"Params: {results_channels['params']}")
    print(f"Estimated results: {results_channels['estimated_results']}")
    print(f"Loaded items: {results_channels['loaded_items']}")
    channels = [item for item in results_channels['items'] if item['type'] == 'channel']
    print(f"Channels: {len(channels)}")
    for channel in channels[:3]:
        print(f"  Channel: {channel['title']} - {channel.get('subscriberCount', 'N/A')}")
    print()

    # Example 3: Search videos uploaded today
    print("=== Search Videos Uploaded Today ===")
    search_today = Search("Python programming", max_results=10, filter=SearchFilters.VIDEOS_TODAY)
    search_today.perform_search()
    results_today = search_today.get_results()
    print(f"Query: {results_today['query']}")
    print(f"Filter: {results_today['filter']} (Videos uploaded today)")
    print(f"Params: {results_today['params']}")
    print(f"Estimated results: {results_today['estimated_results']}")
    print(f"Loaded items: {results_today['loaded_items']}")
    print()

    # Example 4: Search sorted by upload date
    print("=== Search Sorted by Upload Date ===")
    search_date = Search("Python programming", max_results=10, filter=SearchFilters.SORT_BY_DATE)
    search_date.perform_search()
    results_date = search_date.get_results()
    print(f"Query: {results_date['query']}")
    print(f"Filter: {results_date['filter']} (Sorted by upload date)")
    print(f"Params: {results_date['params']}")
    print(f"Estimated results: {results_date['estimated_results']}")
    print(f"Loaded items: {results_date['loaded_items']}")
    print()

    # Save one example to file
    with open("search_filtered_example.json", "w", encoding="utf-8") as f:
        json.dump(results_channels, f, indent=4, ensure_ascii=False)

    print("Filtered search results saved to search_filtered_example.json")

if __name__ == "__main__":
    main()