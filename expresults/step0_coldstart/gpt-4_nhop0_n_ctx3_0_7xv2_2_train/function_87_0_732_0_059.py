
import re

def is_spam(text):
    spam_indicators = [
        r'(광고)',
        r'https?:\/\/\S*',
        r'지금 바로 가입하세요',
        r'\d{1,3}%\s*수익',
        r'(오늘|내일).*?\d{1,2}시부터',
        r'(!?익절!?|익절하세요)',
        r'\*\*(.)*',
        r'(선착순)'
    ]

    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True
    return False
