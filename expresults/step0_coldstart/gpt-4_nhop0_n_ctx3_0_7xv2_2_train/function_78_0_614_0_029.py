
import re

def has_short_url(text):
    short_url_pattern = 'https?://([a-z0-9]+\.)?(me2|dokdo)\.kr/[^\s]+'
    return bool(re.search(short_url_pattern, text))

def has_money(text):
    money_pattern = '[\d]+만원'
    return bool(re.search(money_pattern, text))

def has_ad(text):
    ad_pattern = '\(광고\)'
    return bool(re.search(ad_pattern, text))

def has_unsub(text):
    unsub_pattern = '무료거부|정확한 분석|검증된 수익률'
    return bool(re.search(unsub_pattern, text))

def is_spam(text):
    return has_short_url(text) or has_money(text) or has_ad(text) or has_unsub(text)
