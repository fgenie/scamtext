
import re

def is_spam(text: str) -> bool:
    spam_pattern1 = re.compile(r"\[(?:광고|Advertisement)\]")
    spam_pattern2 = re.compile(r"\*[^\*]*\*")
    spam_pattern3 = re.compile(r"http[s]?:\/\/\S+")

    if spam_pattern1.search(text) or spam_pattern2.search(text) or spam_pattern3.search(text):
        return True
    else:
        return False
