def is_spam(message):
    import re

    spam_filters = [
        r'https?:\/\/\S+',  # URL
        r'\d+\s*[만만원]|완료함',  # Amount, currency
        r'\d+Δ로',  # Special characters
        r'\++상한가|\++상승|적\u0001|루징|하한가 일|적중',  # Stock trading terms
        r'무료상담|무료체험|정보방|①|\②',  # Promotions
        r'특별정보방',  # Special information
        r'성투|직접판단하세요', # Achievements
        r'무료배송', # Free shipping
        r'디젠스|입원관심요망|차별화된 전략', # Products
    ]

    for spam_filter in spam_filters:
        if re.search(spam_filter, message):
            return True

    return False