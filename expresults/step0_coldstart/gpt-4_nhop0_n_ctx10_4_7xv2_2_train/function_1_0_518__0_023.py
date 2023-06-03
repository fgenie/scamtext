
import re

def is_spam(message):
    # Check for urls
    url_regex = r"https?://[A-Za-z0-9./]+"
    has_url = bool(re.search(url_regex, message))
    
    # Check for excessive use of special characters
    special_chars = r"[!@#$%^&*()_+]+"
    excessive_special_chars = bool(re.search(special_chars * 3, message))

    # Check for common spam keywords
    spam_words = ["상한가", "급등예정", "매수시점", 
                  "체험방", "추천주", "수익", "상상플러스",
                  "비밀번호", "선물투자", "입장코드",
                  "무료거부", "프로매매", "투자방",
                  "프로부장", "증권사", "VIP"]
    has_spam_word = any(word in message for word in spam_words)

    # Check for urls with spam keywords and a small message length
    url_spam_words = ["bit.ly", "me2.kr", "gg.gg", "han.gl"]
    small_message_length = len(message) <= 100
    has_url_spam_word = any(word in message for word in url_spam_words)
    
    # If any of the characteristics is found in the message, classify as spam
    if has_url and (excessive_special_chars or has_spam_word or (has_url_spam_word and small_message_length)):
        return True
    else:
        return False
