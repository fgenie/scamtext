
import re


def is_spam(message: str) -> bool:
    spam_indicators = [
        r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'\d{10}',
        r'(?:광고|무료거부|만료시)',
        r'(?:\{\{|\}\}|\[\[|\]\]|\(\(|\)\)|◆|▲|▶|▼|◎|※|!!!|\([\w\d\s,\{\}=+_\-.@&%\$《★;`"<」)(\[\])]*)'
    ]

    regex = '|'.join(spam_indicators)
    if re.search(regex, message, re.MULTILINE):
        return True
    else:
        return False
