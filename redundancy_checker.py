import hashlib

def get_hash(data: str) -> str:
    """Generate SHA-256 hash of the data"""
    return hashlib.sha256(data.strip().lower().encode()).hexdigest()

def is_redundant(data: str, existing_hashes: set) -> bool:
    """Check if data is already in the database based on hash"""
    data_hash = get_hash(data)
    return data_hash in existing_hashes
