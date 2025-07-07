def classify_call(msg):
    msg_lower = msg.lower()
    if "missed" in msg_lower:
        return "missed"
    elif "call started" in msg_lower or "video call started" in msg_lower:
        return "successful"
    else:
        return "other"
    
import re
def extract_call_duration(msg):
    msg = msg.lower()
    hours = 0
    minutes = 0

    hr_match = re.search(r'(\d+)\s*hr', msg)
    min_match = re.search(r'(\d+)\s*min', msg)

    if hr_match:
        hours = int(hr_match.group(1))
    if min_match:
        minutes = int(min_match.group(1))

    total_minutes = hours * 60 + minutes
    return total_minutes


def extract_call_duration(msg):
    msg = msg.lower()
    hours = 0
    minutes = 0

    hr_match = re.search(r'(\d+)\s*hr', msg)
    min_match = re.search(r'(\d+)\s*min', msg)

    if hr_match:
        hours = int(hr_match.group(1))
    if min_match:
        minutes = int(min_match.group(1))

    total_minutes = hours * 60 + minutes
    return total_minutes


def classify_direction(row,your_name,  friend_name):
    msg = row['clean_msg']
    sender = row['username']
    
    if "voice call. no answer" in msg:
        # You initiated a call, they didn't answer
        if sender == your_name:
            return f"{your_name} → missed by {friend_name}"
    elif "missed voice call" in msg:
        # They called you, you missed it
        if sender == friend_name:
            return f"{friend_name} → missed by {your_name}"
    
    return "unknown"


def clean_message(msg):
    # Remove invisible Unicode characters (zero-width space, LRM, etc.)
    return re.sub(r'[\u200e\u200f\u202a-\u202e]', '', msg).strip().lower()