
import re

def is_spam(text):
    # Check for signs of spam
    spam_words = ['광고', '지원금', '입장코드', '상한가', '수익률', '안전거래', '경품', '당첨', '무료체험', '회원가입', '추천']
    spam_url_pattern = r'https?://\S*'
    phone_number_pattern = r'\d{2,4}-\d{3,4}-\d{4}'

    text = text.lower()

    # Count number of spam words and check for spam URLs and phone numbers in the text
    spam_count = 0
    for word in spam_words:
        spam_count += text.count(word.lower())

    urls = re.findall(spam_url_pattern, text)
    phone_numbers = re.findall(phone_number_pattern, text)

    # Classify as spam if at least two spam words or one spam word with spam url or phone number
    if spam_count >= 2 or (spam_count >= 1 and (len(urls) > 0 or len(phone_numbers) > 0)):
        return True
    else:
        return False
