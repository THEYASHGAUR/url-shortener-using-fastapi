# URL Shortener using FastAPI

A simple and efficient URL shortener service built with FastAPI and SQLite.

## Features
- Shorten long URLs to compact, easy-to-share links
- Permanent redirects to original URLs
- SQLite database for storage
- FastAPI-powered API with automatic documentation

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
# Using the built-in FastAPI server
python -m app.main
# The server will start at http://localhost:8000
```

## How to Use

### API Documentation
Visit http://localhost:8000/docs to access the interactive API documentation.

### Shorten a URL
1. Open http://localhost:8000/docs
2. Go to POST /shorten endpoint
3. Enter your URL in the following format:
```json
{
    "original_url": "https://your-long-url.com"
}
```
4. The response will contain your shortened URL

### Access Shortened URL
Simply open the shortened URL in your browser, and you'll be redirected to the original URL.

## Project Structure
```
app/
├── routes/
│   └── url_routes.py    # API endpoints
├── database.py          # Database configuration
├── main.py             # FastAPI app initialization
├── models.py           # Database models
├── schema.py           # Pydantic models
└── utlis.py           # Utility functions
```

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Hashids
