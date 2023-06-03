
import re

def is_spam(text):
    spam_patterns = [
        r'\d{6,}',                        # Long digit strings
        r'[sS][uU][bB][sS][cC][rR][iI][bB][eEvVeE0투이2][rR]', # Obfuscated "subscribe"
        r'[eE3][aA][rR][nN]',             # Obfuscated "earn"
        r'[fF][rR][eE3][eE]',             # Obfuscated "free"
        r'$[iI1][nN][vV][eE3][sS][tT]',    # Obfuscated "invest"
    ]

    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True
    return False
