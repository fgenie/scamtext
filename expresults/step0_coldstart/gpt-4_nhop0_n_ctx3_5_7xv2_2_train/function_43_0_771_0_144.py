
import re

def is_spam(text):
    # Searching for suspicious patterns
    spam_patterns = [
        r"확인▼",
        r"https?://[\w.]+/\w+",
        r"☞",
        r"[<>~※㉿◎◎===▷▶↓⇒]",
        r"[①②③④⑤⑥⑦⑧⑨⑩]",
        r"[＆＋]",
        r"[♥️💓❤️💘]",
        r"\d{1,2}만",
        r"입금",
        r"출금",
        r"종목",
    ]

    for pattern in spam_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False
