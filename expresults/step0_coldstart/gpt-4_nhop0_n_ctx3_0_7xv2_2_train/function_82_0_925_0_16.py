
import re

def is_spam(message):
    # Look for common spam patterns
    spam_patterns = [
        r"(?i)(VIP|투자체험|목표가|최소 | 이상상승 | 종목 정보 | 오전에 공시발표|광고)", # Spam keywords
        r"\bhttps?://\S+", # URLs
        r"\b(080|(\d{3}))[0-9]+", # Phone numbers starting with 080
        r"(\d{1,3}(,\d{3})*(\.\d{2})?)", # Currency values
        r"[A-Z]{2,}", # All CAPS words
        r"\d+(\.\d+)?%"] # Percentage values
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    return False
