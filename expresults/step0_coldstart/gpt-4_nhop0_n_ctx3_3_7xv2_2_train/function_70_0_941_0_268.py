
import re

def is_spam(message):
    # Check for unusual URLs
    unusual_url = re.search(r'(?:https?:\/\/)?(?:[\w-]*\.)+[a-z]{2,}(?:\/[-\w%+.~]+)*', message, re.IGNORECASE)

    # Check for excessive use of special characters
    special_chars = re.findall(r'[\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]', message)

    # Check for obfuscated words or phrases
    obfuscated_chars = re.findall(r'[\#]?[\^]?[ \.]+[\#]?[\^]?[ ]*', message)

    # Check for phrases related to finance, investments, or winning
    financial_phrases = re.findall(r"(돈|투자|혜택|월급|수익|지원|계약|행복|보너스|지급)", message)

    if unusual_url or len(special_chars) > 5 or len(obfuscated_chars) > 5 or len(financial_phrases) > 0:
        return True
    else:
        return False
