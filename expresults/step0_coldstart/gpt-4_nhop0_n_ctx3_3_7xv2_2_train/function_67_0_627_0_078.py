
import re

def is_spam(input_message: str) -> bool:
    # Default values for each spam indicator
    spam_indicators = {
        "has_url": False,
        "has_email": False,
        "has_phone_number": False,
        "has_words_percentage": 50,
    }
    
    # Regular expression patterns to detect the different spam indicators
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_pattern = re.compile(r'((\+?[0-9]{1,3}[-.\s]?)?([0-9]{2,4}[-.\s]?)?([0-9]{2,4}[-.\s]?)?[0-9]{2,4}(/[0-9]{0,7})?)')
    
    # Check for each spam indicator in the input_message
    spam_indicators["has_url"] = bool(url_pattern.search(input_message))
    spam_indicators["has_email"] = bool(email_pattern.search(input_message))
    spam_indicators["has_phone_number"] = bool(phone_pattern.search(input_message))

    # Tokenize the message and count words and digits
    words = input_message.split()
    digits = sum(c.isdigit() for c in input_message)
    if len(words) > 0:
        spam_indicators["has_words_percentage"] = (digits / len(words)) * 100
    else:
        spam_indicators["has_words_percentage"] = 0

    # A message is considered spam if it meets at least two of the following conditions:
    # 1. Contains URLs
    # 2. Contains email addresses
    # 3. Contains phone numbers
    # 4. The percentage of words consisting of digits is greater than 50%
    spam_count = sum(value for key, value in spam_indicators.items() if key != "has_words_percentage")
    return spam_count >= 2 or spam_indicators["has_words_percentage"] >= 50
