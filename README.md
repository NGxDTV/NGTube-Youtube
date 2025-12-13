# NGTube – YouTube Scraper

A comprehensive Python library for scraping YouTube data, including **videos, comments, channels, shorts, and search results**, without using the official YouTube Data API.

NGTube focuses on **structured, continuation-based extraction** and is designed for developers who need **complete and reproducible datasets** for research, analysis, or tooling.

---

## ⚠️ Disclaimer

**This project is provided strictly for educational and research purposes.**

Scraping YouTube may violate YouTube’s Terms of Service. By using this library, you acknowledge that:

* You are responsible for complying with YouTube’s Terms of Service
* You use this library at your own risk
* The author is not liable for misuse or legal consequences

Always respect `robots.txt`, apply **rate limiting**, and avoid abusive traffic.

---

## Why NGTube?

NGTube is **not** a downloader. It is a **low-level data scraper** designed for completeness and transparency.

Key differentiators:

* No official YouTube API key required
* Continuation-based pagination (comments, videos, shorts)
* Full channel profile extraction
* Shorts scraping with metadata + comments
* Country & language localization
* Clean, JSON-compatible output
* Modular, class-based design

---

## Features

* **Video Extraction**
  Extract full video metadata (title, views, likes, duration, tags, description, category, publish dates, etc.)

* **Comment Extraction**
  Load top comments and regular comments, with optional limits or full continuation loading

* **Channel Extraction**
  Extract channel profiles including subscribers, description, featured video, banners, avatars, and full video lists

* **Shorts Extraction**
  Fetch random Shorts from the homepage or load large batches from the Shorts feed, including metadata and comments

* **Search**
  Perform YouTube searches with filters (videos, channels, playlists, upload time, sorting)

* **Country Localization**
  All requests support country and language filters (US, DE, UK, FR, ES, IT, JP, etc.)

* **Flexible Limits**
  Load a fixed number of videos/comments or everything available

* **Structured Output**
  All data is returned as clean, JSON-ready Python dictionaries

---

## Installation

### Recommended

```bash
pip install NGTube
```

Python **3.6+** is required.

Dependencies:

* `requests`
* `demjson3`

---

## Quick Start

### Video Metadata

```python
from NGTube import Video

video = Video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
data = video.extract_metadata()

print(data["title"])
print(data["view_count"])
print(data["like_count"])
print(data["duration_in_seconds"])
```

---

### Comments

```python
from NGTube import Comments

comments = Comments("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Load limited comments (recommended)
data = comments.get_comments(max_comments=50)

for comment in data["comments"][:3]:
    print(comment["author"], comment["text"])
```

⚠️ Avoid loading all comments on very large videos.

---

### Channel Profile

```python
from NGTube import Channel

channel = Channel("https://www.youtube.com/@RickAstleyYT")

profile = channel.extract_profile(max_videos=10)

print(profile["title"])
print(profile["subscribers"])
print(profile["loaded_videos_count"])
```

To load **all** videos:

```python
profile = channel.extract_profile(max_videos="all")
```

---

### Shorts

```python
from NGTube import Shorts, Comments

shorts = Shorts()

short = shorts.fetch_short()
print(short["video_id"], short["title"])

comments = Comments(f"https://www.youtube.com/watch?v={short['video_id']}")
short_comments = comments.get_comments(max_comments=20)
```

Load multiple Shorts from the feed:

```python
feed = shorts.fetch_shorts_feed(max_shorts=20)
```

---

## Data Schemas

### Video Metadata Schema

```python
video_details = {
    "title": None,
    "view_count": None,
    "duration_in_seconds": None,
    "description": None,
    "tags": None,
    "video_id": None,
    "channel_id": None,
    "is_owner_viewing": None,
    "is_crawlable": None,
    "thumbnail": {
        "url": None,
        "width": None,
        "height": None
    },
    "allow_ratings": None,
    "author": None,
    "is_private": None,
    "is_unplugged_corpus": None,
    "is_live_content": None,
    "like_count": None,
    "channel_name": None,
    "category": None,
    "publish_date": None,
    "upload_date": None,
    "family_safe": None,
    "channel_url": None,
    "subscriber_count": None
}
```

---

### Comments Schema

```python
comments_data = {
    "top_comment": {
        "author": None,
        "text": None,
        "dateCreated": None,
        "url": None,
        "alternateName": None,
        "upvoteCount": None
    },
    "comments": {
        "author": None,
        "text": None,
        "likeCount": None,
        "publishedTimeText": None,
        "authorThumbnail": None,
        "commentId": None,
        "replyCount": None
    }
}
```

---

### Channel Profile Schema

```python
channel_data = {
    "featured_video": {
        "videoId": None,
        "title": None,
        "description": None
    },
    "viewCountText": None,
    "videoCountText": None,
    "subscriberCountText": None,
    "banner": {
        "url": None,
        "width": None,
        "height": None
    },
    "title": None,
    "description": None,
    "channelId": None,
    "channelUrl": None,
    "keywords": None,
    "isFamilySafe": None,
    "links": None,
    "avatar": {
        "url": None,
        "width": None,
        "height": None
    },
    "videos": {
        "videoId": None,
        "title": None,
        "publishedTimeText": None,
        "viewCountText": None,
        "lengthText": None,
        "thumbnails": {
            "url": None,
            "width": None,
            "height": None
        }
    },
    "loaded_videos_count": None,
    "subscribers": None,
    "total_views": None,
    "video_count": None
}
```

---

### Shorts Schema

```python
short_data = {
    "channel_name": None,
    "channel_handle": None,
    "channel_id": None,
    "channel_url": None,
    "title": None,
    "sound_metadata": None,
    "comments_continuation": None,
    "view_count": None,
    "publish_date": None,
    "like_count": None,
    "video_id": None,
    "thumbnail": {
        "url": None,
        "width": None,
        "height": None
    },
    "sequence_continuation": None
}
```

---

## Country Filters

Available presets:

* US – United States
* DE – Germany
* UK – United Kingdom
* FR – France
* ES – Spain
* IT – Italy
* JP – Japan

Each filter defines `hl` (language) and `gl` (region).

---

## Limitations

* YouTube may rate-limit requests
* Internal APIs can change at any time
* Loading all comments or videos can be slow
* Shorts use the same comment system as normal videos

Apply delays for large crawls.

---

## Troubleshooting

* Import errors → Ensure NGTube is installed correctly
* Missing fields → Some videos restrict data
* API errors → YouTube internal endpoints may change

---

## Contributing

This project is maintained for educational purposes.

Issues, improvements, and documentation suggestions are welcome.

---

## License

Free to use with attribution.