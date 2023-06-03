import re

def is_spam(message):
    # Check for presence of urls
    url_pattern = re.compile(r'(https?://\S+|www\.\S+)')
    url_count = len(re.findall(url_pattern, message))

    # Check for presence of phone numbers
    phone_pattern = re.compile(r'(\d{2,4}-\d{3,4}-\d{4}|\d{2,4}\s\d{3,4}\s\d{4}|\d{10,11})')
    phone_count = len(re.findall(phone_pattern, message))

    # Check for presence of currency and numbers
    currency_pattern = re.compile(r'(\$|원|￦)')
    currency_count = len(re.findall(currency_pattern, message))
    numbers_pattern = re.compile(r'\d{4,}')
    numbers_count = len(re.findall(numbers_pattern, message))

    # Check for presence of percent signs
    percent_pattern = re.compile(r'(\d{1,3}%|배)')
    percent_count = len(re.findall(percent_pattern, message))

    # Check for presence of key words
    keywords_pattern = re.compile(r'(광고|소?수익|적?힌|나스닥|목표가|투자|작전정보|추천|종목|전세)')
    keywords_count = len(re.findall(keywords_pattern, message))

    # Conditions for spam classification
    if url_count >= 1 or phone_count >= 1 or (currency_count > 0 and numbers_count > 0) or percent_count > 0 or keywords_count > 0:
        return True
    return False