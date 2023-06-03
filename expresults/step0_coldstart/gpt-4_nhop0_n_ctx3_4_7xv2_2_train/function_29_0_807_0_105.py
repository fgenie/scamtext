
import re

def is_spam(message):
    # Pattern for links and special characters
    link_pattern = r"(http|https)://\S+"
    special_chars_pattern = r"[♥️☞＆🎈3️⃣🔟👉⑧⑦ⓒ]"

    # Check for link and special characters
    link_match = re.search(link_pattern, message)
    special_chars_match = re.search(special_chars_pattern, message)

    # Return True if any of the patterns are found, otherwise False
    return bool(link_match or special_chars_match)

