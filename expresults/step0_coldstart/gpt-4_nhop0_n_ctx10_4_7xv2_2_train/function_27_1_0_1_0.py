
import re

def is_spam(text):
    # Check if there are links in the message
    link_pattern = r'(http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    link_count = len(re.findall(link_pattern, text))
    
    # Check for unusual characters and capitalization
    unusual_characters_pattern = r'[\W\d]+'
    unusual_characters_count = len(re.findall(unusual_characters_pattern, text))
    upper_count = sum(map(str.isupper, text))
    
    # Count the number of words in the message
    words = re.findall(r'\w+', text)
    word_count = len(words)
    
    if(link_count >= 2 or
       unusual_characters_count >= int(0.5 * word_count) or
       upper_count >= int(0.4 * len(text))):
        return True
    else:
        return False
