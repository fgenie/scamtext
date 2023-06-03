
import re

def is_spam(message):
    message = message.lower()
    
    # Check for common spam phrases
    spam_phrases = ["무료체험", "정회원", "이사비지원", "루징", "양득", "단폴"]
    if any(spam_word in message for spam_word in spam_phrases):
        return True
    
    # Check for excessive use of special characters
    num_special_chars = len(re.findall(r'[\W]', message))
    if num_special_chars / len(message) > 0.3:
        return True

    # Check for suspicious shortened URLs
    url_pattern = re.compile(r'(http[s]?://\S*)|(bit\.ly/\S*)|(me2\.kr/\S*)')
    if url_pattern.search(message):
        return True
    
    return False
