
import re

def is_spam(text):
    # Check for unusual characters and patterns
    unusual_char_pattern = re.compile(r'[\W\s]+')
    unusual_chars = len(unusual_char_pattern.findall(text))
    unusual_chars_ratio = unusual_chars / len(text)
    
    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    contains_url = bool(url_pattern.search(text))

    # Check for exaggerated expressions (e.g., repeating characters)
    exaggerated_expression_pattern = re.compile(r'(.)\1{2,}')
    exaggerated_expressions = bool(exaggerated_expression_pattern.search(text))

    # Check for words associated with spam (e.g., "free", "promo", etc.)
    spam_keywords = ['무료', '추천', '천만', '반독점', '반값', '당첨', '선물', '프로모션', '종료']
    contains_spam_keywords = any(keyword in text for keyword in spam_keywords)

    # Determine if the message is spam based on the criteria above
    if unusual_chars_ratio > 0.4 or contains_url or exaggerated_expressions or contains_spam_keywords:
        return True
    else:
        return False
