
import re

def is_spam(message: str) -> bool:
    # Check for phrases commonly found in spam messages
    spam_phrases = ["큽", "무료거부", "비밀번호", "마쎤", "lhy852", "안내"]

    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for URL shorteners
    url_shorteners = ["bit.ly", "goo.gl", "tinyurl.com", "me2.kr", "han.gl"]
    regex_shorteners = re.compile("|".join(url_shorteners))
    
    if regex_shorteners.search(message):
        return True

    # Check for an excessive amount of special characters or numbers
    special_chars = '┻]+[＜><「」“”ー`~=∥´¨＾￣０〇＼∀φ□↑↓←→→￢　『』『』『』“”∞￥％＆＊＄＃＠！＾￣￢￣!！＾+【】█▂▃▅▆▇░▒▓▄♨♩♪♭♯♬♱♲♳♴♵♶♮♩Ѡ♯♩♪♫♬♭♩♩♪♫♬♭♮♩♩♪♹♺♼♽♾♯♩♪♫♬♯♯',
    numbers = '0123456789'

    special_count = sum(1 for char in message if char in special_chars)
    number_count = sum(1 for char in message if char.isdigit())
    
    if special_count > len(message) * 0.15 or number_count > len(message) * 0.3:
        return True
    
    # If none of the conditions above are met, classify the message as normal
    return False
