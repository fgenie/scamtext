
import re

def is_spam(message):
    spam_indicators = [
        r'\d{2,4}\S*\d{2,4}\S*\d{2,4}\S*',    # Repeated sequences of digits, possibly separated by non-word characters
        r'http[s]?://\S+',                     # Links that start with "http://" or "https://"
        r'\%|\$',                              # Percentage or Dollar signs
        r'무료거부|증시침체|적중',              # Any of these spam-related keywords: "무료거부", "증시침체", or "적중"
        r'[\s\S]*㈜[\s\S]*'                    # Text that contains the rare abbreviation form "㈜"
    ]

    # Converts message to lowercase
    message = message.lower()

    # Checks if any spam indicator is present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
    return False
