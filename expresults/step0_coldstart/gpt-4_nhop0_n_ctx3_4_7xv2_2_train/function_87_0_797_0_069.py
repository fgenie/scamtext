
import re

def is_spam(message):
    # Check for spam patterns

    # Check if message contains advertisement or invitation codes
    if "광고" in message or "입장코드" in message:
        return True
    
    # Check if message contains urls
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check if message contains high percentage values
    percentage_pattern = re.compile(r'\d{1,3}(%|퍼센트)')
    percentages = re.findall(percentage_pattern, message)
    if len(percentages) > 0:
        return True

    # Check if message contains large numeric values
    large_number_pattern = re.compile(r'[0-9]{6,}')
    large_numbers = re.findall(large_number_pattern, message)
    if len(large_numbers) > 0:
        return True

    # Check if message contains suspicious keywords
    spam_keywords = ["쳣", "지원금", "루징", "요율", "당신", "서두르시면", "이벤트", "증정", "안전하게", "지금바로", "무료거부", "숫자는실시간변동됩니다"]
    for word in spam_keywords:
        if word in message:
            return True

    # If none of the above conditions are met, the message is not spam
    return False
