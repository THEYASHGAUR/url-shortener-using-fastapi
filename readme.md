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


## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Hashids
