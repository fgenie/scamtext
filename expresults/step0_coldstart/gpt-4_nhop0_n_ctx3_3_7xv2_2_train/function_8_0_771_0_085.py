
import re

def is_spam(message):
    # Check for common spam keywords
    spam_keywords = ['기회', '매수', '매도', '수익', '상승', '블록', '주식', '추천', '익절', '선취매', '매매', '테마주', '수급', '수급주', '장담']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for shortened URLs
    shortened_url_pattern = r'han\.gl|me2\.kr|bit\.ly|goo\.gl|ow\.ly'
    if re.search(shortened_url_pattern, message):
        return True

    # Check for unusual symbols
    unusual_symbols = ['▼', '▲', '◆', '+']
    for symbol in unusual_symbols:
        if symbol in message:
            return True

    # Check for repetition of the same character more than 4 times in a row
    if re.search(r'(.)\1{3,}', message):
        return True

    return False
