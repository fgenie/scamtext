
import re

def is_spam(text):
    
    # Use regex for common spam characteristics, such as urls, capitalization, phone numbers, etc.
    url_regex = r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    encoding_regex = r'[^\u0000-\u007f]+'   # non-ascii symbol
    number_regex = r'\d+'
    
    # Detect presence of urls
    url_match = re.search(url_regex, text)
    
    # Detect non-ascii symbols
    encoding_match = re.search(encoding_regex, text)
    
    # Detect excessive numeric characters
    numbers_match = re.search(number_regex, text)
    
    if url_match or encoding_match:
        return True
    
    # Check if the number of numeric characters is more than 50% of the message
    if numbers_match:
        numbers_length = sum([len(match.group()) for match in re.finditer(number_regex, text)])
        if numbers_length / len(text) > 0.5:
            return True

    return False
