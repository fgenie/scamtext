
import re

def is_spam(message):
    # Checks for long-string of characters, uppercases and numbers
    pattern1 = re.compile(r"([A-Za-z0-9_.+-]{15,})")
    
    # Checks for consecutive punctuations
    pattern2 = re.compile(r"([!,.?]{3,})")
    
    # Checks for URL patterns
    pattern3 = re.compile(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
    
    # Checks for large numbers and percentage
    pattern4 = re.compile(r"(백|천|만|억)+|(\d{4,})|(%\s*상승)")
    
    # Checks for monetary symbols followed by a large number
    pattern5 = re.compile(r"원|₩|\$\s*\d{4,}")
    
    if pattern1.search(message) or pattern2.search(message) or pattern3.search(message) or pattern4.search(message) or pattern5.search(message):
        return True
    else:
        return False
