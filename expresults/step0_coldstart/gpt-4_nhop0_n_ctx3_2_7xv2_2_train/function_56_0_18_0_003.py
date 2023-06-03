
import re

def is_spam(message):
    # List of common spam keywords and patterns
    spam_keywords = [
        r'\b[Vv][Ii][Pp]',
        r'\b[Ff][Rr][Ee][Ee]',
        r'\b[Mm][Uu][Ll][Tt][Ii]',
        r'\b[Cc][Hh][Ee][Cc][Kk]',
        r'\b[Cc][Ll][Ii][Cc][Kk]',
        r'\b[Oo][Pp][Ee][Nn]',
        r'\b[Gg][Ii][Vv][Ee]',
        r'\b[Pp][Ee][Rr][Cc][Ee][Nn][Tt]',
        r'\b[Ss][Oo][Vv][Ee][Rr][Ii][Gg]{0,1}[Nn]{0,1}\b',
        r'\b[Pp][Uu][Mm][Pp]',
        r'\b[Bb][Aa][Dd]\b',
    ]

    # Check if any spam keyword is present in the message
    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    # Check if there's a URL containing suspicious domain names
    domain_regex = r'\b(openkakao|bit)\.(it|ly)\b'
    if re.search(domain_regex, message):
        return True

    return False
