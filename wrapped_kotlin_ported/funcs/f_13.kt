fun isSpam(message: String): Boolean {
    val spamIndicators = arrayOf(
        "조아팟",
        "무료수신거부",
        "루멘스",
        "문의",
        "추천",
        "공개",
        "상한가",
        "미리확인",
        "https://",
        "http://",
        "내일 발표",
        "엠바고",
        "상장",
        "이벤트",
        "상품권",
        "파트너",
        "쿠폰",
        "할인",
        "프로모션",
        "프리미엄",
        "기회",
        "출시",
        "방송",
        "매스컴",
        "뉴스",
        "사전등록",
        "마감"
    )

    val lowerCaseMessage = message.toLowerCase()
    var count = 0

    for (indicator in spamIndicators) {
        if (indicator.toLowerCase() in lowerCaseMessage) {
            count++
        }
    }

    return count >= 2
}
