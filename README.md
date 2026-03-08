# wikipedia-dyk-api

An API to serve requests for announcements, articles, and facts listed in [Wikipedia's "Did you know..." page](https://en.wikipedia.org/wiki/Wikipedia:Recent_additions).

**Contents**

- [Setup](#setup)
- [Run locally](#run-locally)
- [License](#license)

## Description

Wikipedia's [front page](https://en.wikipedia.org/wiki/Main_Page) has a section called, "Did you know...", which showcases quick hooks for recently expanded articles.

Currently, there is an [archive page](https://en.wikipedia.org/wiki/Wikipedia:Recent_additions) that allows you to search from February 2004 until now. But they are not accessible by queries or any other means besides a simple search.

This project here aims to make these hooks and recent additions to Wikipedia accessible through an API.

## Getting Started

### Dependencies

- Python 3.10+
- FastAPI

### Setup

```bash
python3 -m venv wikidyk
```

### Installing

```bash
source wikidyk/bin/activate
pip install -r requirement.txt
```

### Running

Run development:

```bash
fastapi dev
```

Access the documentation page for this API using http://127.0.0.1:8000/docs.

## License

MIT
