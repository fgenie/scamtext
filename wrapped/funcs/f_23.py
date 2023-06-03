
import re

def is_spam(message):
    # Check for unusual characters and patterns often found in spam
    if re.search(r"[^\w\s.!?]", message):
        return True
    
    # Check if the message contains a suspicious URL
    if re.search(r"http(s)?://[^\s]+", message):
        return True
    
    # Check if the message contains congratulatory phrases often found in spam
    if re.search(r"축하(합니다|드립니다)", message):
        return True

    # Check if the message contains secretive phrases often found in spam
    if re.search(r"극비|차별화 된|무료로", message):
        return True

    # Check if the message contains financial promises often found in spam
    if re.search(r"수익|올랐다|상한가 확정|최신종목", message):
        return True

    # If none of the above conditions are met, it is not spam
    return False
