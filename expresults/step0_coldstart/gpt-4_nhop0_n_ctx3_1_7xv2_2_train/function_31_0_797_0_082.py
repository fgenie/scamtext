
import re

def is_spam(message):
    # Case 1: Check for alphanumeric repeated sequences
    alphanumeric_repeated_seq = r'[a-zA-Z0-9]{3,}.([a-zA-Z0-9]+[\W]*[^a-z]{2,}){2,}'
    if re.search(alphanumeric_repeated_seq, message, re.IGNORECASE):
        return True

    # Case 2: Check for shortened URLs
    shortened_urls = r'((https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?)'
    if re.search(shortened_urls, message) and message.count("/") > 3:
        return True

    # Case 3: Check for percentage and large amounts of money
    percentage_large_money = r'(?:(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)|\d{%2C})(\s*\%|\s*\b원\b)'
    if re.search(percentage_large_money, message):
        return True

    # Case 4: Check for phone numbers
    phone_numbers = r'(\d{2,3}\-?\d{3,4}\-?\d{3,4})|(\(\d{2,3}\)\d{3,4}\-?\d{3,4})'
    if len(re.findall(phone_numbers, message)) > 1:
        return True

    # If none of the conditions is met, it is a normal message
    return False
