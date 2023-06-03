
import re

def is_spam(message):
    spam_keywords = [
        '광고', '추천주', '최소', '상승', '목표달성', '공개', '통합운영',
        '제한참여', '기존정보', '혜택유지', '무료', '거부', '고효율'
    ]

    normal_keywords = [
        '송장번호', '보내는분', '상품명', '위탁장소', '배송일자',
        '안녕하세요', '결제 금액', '미입금', '주문취소', '등록기간',
        '등록방법', '학교운영', '행정실'
    ]

    message = re.sub(r'https?:\/\/\S*', '', message)  # removes urls
    message = re.sub(r'\d+', '', message)  # removes numbers
    message = message.lower()

    counter_spam = sum(keyword in message for keyword in spam_keywords)
    counter_normal = sum(keyword in message for keyword in normal_keywords)

    return counter_spam > counter_normal
