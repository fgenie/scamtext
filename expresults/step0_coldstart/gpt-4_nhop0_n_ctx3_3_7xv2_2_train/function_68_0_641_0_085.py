def is_spam(message: str) -> bool:
    import re
    
    # Detect potential spam patterns commonly found in spam messages
    spam_patterns = [
        r'\d+퍼\.*센\.*트', # 퍼센트 표현.
        r'http[s]?:\/\/[\w\.\-\/]+', # urls
        r'\d+\([월화수목금토일]+\)', # 요일 표기.
        r'[Ｂ]\w+\-*\d+[\.\,]{0,1}\w*', # 이상한 문자 혼합
        r'\d{3,}-*\d{3,}', # 연속적인 숫자
        r'^([가-힣]).\1{1,}.*', # 한글+마침표+반복.
        r'광고|인테리어|포함 환경|상품|가입하시|상담|문의|에너지|설계|시공|신제품|특별관', # 일반적인 스팸 단어
        r'KB|SK77|광고', # 특정 문자열
        r'\n\n', # 빈줄
        r'!\n+', # 느낌표
    ]
    
    counter = 0
    for pattern in spam_patterns:
        counter += len(re.findall(pattern, message))
        if counter >= 2:
            return True

    return False