
import re

def is_spam(text):
    keywords = ['추천', '적중', '온라인', '게임', '적중', '포인트', 'VIP', '신규 첫충', '무제한 충전']
    expression = r'(https?://[^\s]+)'
    url_count = len(re.findall(expression, text))

    if url_count > 0 or any(keyword in text for keyword in keywords):
        return True
    else:
        return False
