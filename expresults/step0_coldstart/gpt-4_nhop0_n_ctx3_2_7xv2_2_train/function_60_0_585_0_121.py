
import re

def is_spam(text):
    # Define spam characteristics
    spam_keywords = ['수익', '상한가', '테마주', '종목', '차트', '계속 통화중이더만', '카카오톡', '부자']
    spam_links_patterns = ['opcn-kakao.com', 'openkakao.at']
    many_digits = r'\d{4,}'
    
    # Check if there are spam keywords in the text
    for keyword in spam_keywords:
        if keyword in text:
            return True
            
    # Check if there are spam links in the text
    for pattern in spam_links_patterns:
        if re.search(pattern, text):
            return True
            
    # Check if there are many consecutive digits in the text
    if re.search(many_digits, text):
        return True

    # Not spam
    return False
