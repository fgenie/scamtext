
import re

def is_spam(message):
    # Check for URLs
    urls = re.findall(r'(https?://\S+)', message)

    # Check for unusual characters
    unusual_chars = re.findall(r'[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\s\.,?!]', message)

    # Check for too many special characters and line breaks
    special_chars = re.findall(r'[\W_]', message)
    line_breaks = re.findall('\n', message)
    
    if (len(urls) > 0 or len(unusual_chars) > 0) and (len(line_breaks) >= len(special_chars) / 2):
        return True
    else:
        return False
