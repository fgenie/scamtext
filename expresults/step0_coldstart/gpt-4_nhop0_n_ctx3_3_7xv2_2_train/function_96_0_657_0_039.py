
import re

def is_spam(message: str) -> bool:
    # Regular expression patterns to detect spam
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    openkakao_pattern = re.compile(r'openkakao\.at/\S+')
    unicode_pattern = re.compile(r'[\u3131-\u318E\uAC00-\uD7A3]+')
    sequential_char_pattern = re.compile(r'([가-힣])\1{2,}')

    # Check if the message contains a URL
    if url_pattern.search(message):
        return True

    # Check if the message contains an openkakao link
    if openkakao_pattern.search(message):
        return True

    # Check if the message contains Korean characters
    if not unicode_pattern.search(message):
        return False

    # Check if the message contains sequential repetitions of the same character
    if sequential_char_pattern.search(message):
        return True

    return False
