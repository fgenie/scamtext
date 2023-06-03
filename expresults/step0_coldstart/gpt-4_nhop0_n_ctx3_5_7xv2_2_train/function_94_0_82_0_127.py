
import re

def is_spam(message):
    spam_keywords = ["광고", "추천주", "시황", "이벤트", "알파고", "챗 GPT", "투자", "수익률", "털어라", "채팅물론", "대출상품", "대출한도", "무료거부"]
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(],|]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    
    message = message.replace("\n", " ")
    
    # If the message contains a URL, it might be spam
    if url_pattern.search(message):
        return True
    
    # If the message contains multiple spam keywords, it might be spam
    spam_keyword_count = 0
    for keyword in spam_keywords:
        if keyword in message:
            spam_keyword_count += 1
            if spam_keyword_count >= 3:
                return True
    
    # If the message is all uppercase or has a high count of special characters, it might be spam
    if message.isupper() or len(re.findall(r"[^a-zA-Z0-9가-힣\s]", message)) > 5:
        return True

    return False
