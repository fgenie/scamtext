
import re

def is_spam(text):
    # Keywords that might be common in spam messages
    spam_keywords = ['수익', '추천', 'VIP', '계열사', '상한가', '자유롭게', 'http', '코드', '금액']
    
    # Threshold to decide if a message is spam or not
    spam_threshold = 3

    # Count the occurrence of spam keywords in the text
    spam_counter = 0
    for keyword in spam_keywords:
        if keyword in text:
            spam_counter += 1

    # If spam keywords occurrences are more than the threshold, return True (is spam)
    if spam_counter >= spam_threshold:
        return True

    # Use regular expression to match patterns common in spam messages, such as long URLs, phone numbers or percentages
    url_pattern = 'https?:\/\/\S+'
    phone_pattern = '\d{2,4}-\d{2,4}-\d{2,4}'
    percentage_pattern = '\d{1,3}%'

    # If any common spam patterns are found, return True (is spam)
    if re.findall(url_pattern, text) or re.findall(phone_pattern, text) or re.findall(percentage_pattern, text):
        return True

    return False
