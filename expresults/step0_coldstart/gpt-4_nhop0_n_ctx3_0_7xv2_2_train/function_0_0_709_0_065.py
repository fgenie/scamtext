
import re

def is_spam(message):
    spam_patterns = [r'(주식|타점|익절|지금제한|거래소제한|종목확인|회사공시|목표가|투자|수익률)',
                     r'\d{2,}%\s*이상?', r'https://\S+', r'\[클릭 종목확인\]']

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False
