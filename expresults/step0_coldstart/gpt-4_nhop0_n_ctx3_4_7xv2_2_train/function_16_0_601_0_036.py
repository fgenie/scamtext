
import re

def is_spam(message):
    # Patterns to identify spam messages
    url_pattern = r'https?://\S+'
    short_url_pattern = r'(bit\.ly|t\.co|t\.ly|me2\.kr|vvvkauy\.com|openkakao\.at)/\S+'
    money_pattern = r'([1-9][0-9]{0,2}(?:,\d{3})*원)|([1-9][0-9]{0,2}(?:.\d{3})*원)'
    special_word_pattern = r'(상한가|모의투자|어머님|회원방|정정회원입장)'

    # Check if the message contains any of the spam patterns
    if re.search(url_pattern, message) and re.search(short_url_pattern, message):
        return True
    if re.search(money_pattern, message):
        return True
    if re.search(special_word_pattern, message):
        return True

    return False
