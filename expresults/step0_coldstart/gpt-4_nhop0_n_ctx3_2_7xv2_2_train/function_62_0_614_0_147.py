
import re

def is_spam(message):
    # Check for URL with unusual characters
    url_pattern = r'https?://[\w.-/]*[\W]{2,}[0-9a-zA-Z]*'
    url_match = re.search(url_pattern, message)
    
    # Check for unusual amount of special characters, exclamations or question marks
    special_char_pattern = r'[^A-Za-z0-9가-힣\s\.,?!]+'
    special_chars = re.findall(special_char_pattern, message)
    total_special_chars = sum([len(char_group) for char_group in special_chars])
    too_many_special_chars = total_special_chars / len(message) > 0.20
    
    # Check for potential numeric percentages or profits
    percentage_pattern = r'\d{2,3}%|\d{2,3}(,|.)\d{3}'
    numeric_percentages = re.search(percentage_pattern, message)

    return bool(url_match) or too_many_special_chars or bool(numeric_percentages)
