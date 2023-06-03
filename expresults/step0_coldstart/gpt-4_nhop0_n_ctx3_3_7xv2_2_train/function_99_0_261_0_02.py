
import re

def is_spam(message):
    spam_indicators = [
        r'(상한가|B기업|제휴협약|발표시|3상)',
        r'(사이버 머니|황금알|수익률|무료거부|종목 추천)',
        r'(美FDA 승인|정부 지원|신약 개발)',
    ]
    url_pattern = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url_regex = re.compile(url_pattern)

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    urls_in_message = url_regex.findall(message)
    if urls_in_message and len(urls_in_message) > 1:
        return True

    return False
