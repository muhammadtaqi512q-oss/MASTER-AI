import re

# Initial Users Data
USERS = {
    "Muhammad TAQI": {"password": "Muhammad Taqi512", "balance": 500000, "stars": 0, "level": 1},
    "OLIVIA": {"password": "OLIVIA786", "balance": 200000, "stars": 0, "level": 1},
    "JACK": {"password": "JACK123", "balance": 500000, "stars": 0, "level": 1}, # Default pass added
    "THUNDER": {"password": "THUNDER123", "balance": 700000, "stars": 0, "level": 1},
    "WILLIAM": {"password": "WILLIAM123", "balance": 500000, "stars": 0, "level": 1},
    "ELIZBETH": {"password": "ELIZBETH123", "balance": 800000, "stars": 0, "level": 1},
    "ZIRA": {"password": "ZIRA123", "balance": 1000000, "stars": 0, "level": 1},
    "LYRA HEAD MANAGER OF NEXURA": {"password": "LYRA123", "balance": 3500000, "stars": 0, "level": 1},
    "AHMED": {"password": "AHMED123", "balance": 50000, "stars": 0, "level": 1},
    "OWNER": {"password": "OWNERMASTEROKDONE", "balance": 10000000, "stars": 0, "level": 1}
}

def calculate_cipher_password(username, domain):
    """
    Calculates password where a=1, b=2... z=26 for username + domain
    """
    combined = (username + domain).lower()
    clean_text = re.sub(r'[^a-z]', '', combined) # Only characters
    
    password_parts = []
    for char in clean_text:
        val = ord(char) - ord('a') + 1
        password_parts.append(str(val))
        
    return ",".join(password_parts)
