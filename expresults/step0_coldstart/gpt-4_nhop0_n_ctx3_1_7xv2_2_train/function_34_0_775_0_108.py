
import re

def is_spam(message):
    # Check for spam keywords and short URLs
    spam_keywords = ["매집", "비밀", "종목", "공개", "최신", "정보", "공시", "상한가",
                     "계약", "주식", "추천", "시황", "실력", "입증", "VIP"]
    short_url_pattern = r"https?://[\w./?=]+"
    short_url = re.search(short_url_pattern, message)

    # Check if message contains any spam keywords or short URLs
    if any(keyword in message for keyword in spam_keywords) or short_url:
        return True
    else:
        return False
