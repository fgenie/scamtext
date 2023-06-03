
import re

def is_spam(text):
    # Detect spam patterns such as repetitions and excessive special characters
    pattern = re.compile(r'(\w|\-|_)*[\w]{2,}(\1)+', re.IGNORECASE)
    repetition_matches = pattern.findall(text)

    # Detect suspicious URLs
    pattern = re.compile(r'((http(s)*:\/\/)?(www\.)?([a-z0-9-_]+)+\.[a-z]+[^\w\s]+)')
    url_matches = pattern.findall(text)

    # Extra check for risky URLs with invitation for clicks or suspicious wording
    risky_words = ["극비", "선착순", "신청", "내일", "수익", "보장"]
    risky_word_pattern = "|".join(risky_words)
    pattern = re.compile(risky_word_pattern, re.IGNORECASE)
    risky_word_matches = pattern.findall(text)

    # If repetitions found or suspicious URLs with risky words are found, consider it as spam
    if repetition_matches or (url_matches and risky_word_matches):
        return True

    return False
