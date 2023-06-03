def is_spam(message):
    import re
    
    # Check for spam features in the message
    spam_features = [
        r'\d{1,2}[.월日]%+',   # Percentage and date-like patterns, e.g. "40%", "17日"
        r'[a-zA-Z\d]{4,}',     # Alphanumeric sequences of 4 or more characters
        r'https?://\S+',       # URLs
        r'\S{5,}@\S+',         # Unusual email addresses
        r'\b[A-Za-z0-9]{5,}\b' # Consecutive 5 or more alphanumerics separated by space or word boundary
    ]
    
    # Check for normal features in the message
    normal_features = [
        r'[가-힣]+',            # Korean characters
        r'(\w+\s?){1,3}',       # Up to 3 words (with or without spaces)
        r'(\d{1,2}[:시반])+',    # Numeric time, e.g. "4시", "8시반"
    ]
    
    # Count occurrences of spam and normal features
    spam_count = 0
    normal_count = 0
    for feature in spam_features:
        spam_count += len(re.findall(feature, message))

    for feature in normal_features:
        normal_count += len(re.findall(feature, message))
    
    # Determine if the message is spam
    if spam_count > normal_count:
        return True
    else:
        return False