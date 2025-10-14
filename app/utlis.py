from hashids import Hashids

# Initialize Hashids (can set your own salt)
hashids = Hashids(min_length=6, salt="fastapi-url-shortener")

def generate_short_code(id: int) -> str:
    return hashids.encode(id)
