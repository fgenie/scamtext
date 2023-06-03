
import re

def is_spam(message: str) -> bool:
    
    def url_count(text: str) -> int:
        url_pattern = re.compile(
            r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
        return len(url_pattern.findall(text))

    def consecutive_count(text: str) -> int:
        consecutive_pattern = re.compile(r"[.?!]{2,}")
        return len(consecutive_pattern.findall(text))

    def special_char_count(text: str) -> int:
        special_char_pattern = re.compile("[%$^#@&*]")
        return len(special_char_pattern.findall(text))
        
    def invalid_char_count(text: str) -> int:
        invalid_char_pattern = re.compile(r"[^a-zA-Z0-9가-힣\s.,>/<;'()\[\]{}\-_!?:$%*&^#@]+")
        return len(invalid_char_pattern.findall(text))

    message = message.strip().lower()
    url_counter = url_count(message)
    consecutive_counter = consecutive_count(message)
    special_char_counter = special_char_count(message)
    invalid_char_counter = invalid_char_count(message)

    
    if url_counter > 1 or consecutive_counter > 0 or special_char_counter > 2 or invalid_char_counter > 1:
        return True
    return False
