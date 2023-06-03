
import re

def is_spam(message):
    # Conditions to classify a message as spam:
    # 1. Presence of numbers and special characters in the message
    # 2. Presence of url shorteners (me2.kr, ko.gl, etc.)
    # 3. Presence of keywords related to stock, money, and percentage increase

    # Regex patterns
    number_special_pattern = r"[0-9!@#$%^&*()_+=,./<>?'\";:{}\[\]|`~]+"
    url_shorteners_pattern = r"(http|https)://(me2.kr|ko.gl)/\S*"
    keywords_pattern = r"(추천주|상한가|코 인/단 타/소 액|화성|%↑|돌파)"

    # Check if any of the conditions are met
    if re.search(number_special_pattern, message) \
            and re.search(url_shorteners_pattern, message) \
            or re.search(keywords_pattern, message):
        return True
    else:
        return False

# Note: Add test cases or further use of the function outside of this code block.
