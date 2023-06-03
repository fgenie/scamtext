
from typing import List
import re

class TextProcessor:
    def __init__(self, spam_keywords: List[str] = None):
        if spam_keywords is None:
            spam_keywords = ['클릭', '경품', '바로가기', '축하합니다']
        self.spam_keywords = spam_keywords

    def has_spam_keyword(self, text: str) -> bool:
        return any(keyword in text for keyword in self.spam_keywords)

    def has_url(self, text: str) -> bool:
        url_pattern = r'(https?:\/\/[^\s]+)|(www\.[^\s]+)'
        return bool(re.search(url_pattern, text))

    def is_spam(self, text: str) -> bool:
        return self.has_spam_keyword(text) and self.has_url(text)

processor = TextProcessor()

def is_spam(message: str) -> bool:
    return processor.is_spam(message)
