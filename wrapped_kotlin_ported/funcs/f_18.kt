import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    // Check for suspicious keywords
    val spamKeywords = arrayListOf(
        "상한가", "상담하기", "적중완료", "준법감시인", "보상 하겠습니다", "분석,상담,진단", "개구리핵심정보",
        "클릭률", "확정", "모바일서비스 이용중지", "10분 외", "추첨", "주식비결", "무상", "신규정보",
        "거래량 폭등", "증 권", "전략 마감임박", "직접판단하세요", "수익률", "연 금"
    )

    for (keyword in spamKeywords) {
        if (message.contains(keyword)) {
            return true
        }
    }

    // Check for URLs with suspicious formats
    val urlPattern: Pattern = Pattern.compile("https?://\\S+")
    val urls: List<String> = urlPattern.matcher(message).usefulStream().toList()

    val suspiciousFormats = arrayListOf(
        "me2.kr", "bit.ly", "openkakao", "buly.kr", "vo.la", "ko.gl", "opcn-kakao.com", "me.shinhan",
        "me2.kr", "openkakao.at"
    )

    for (url in urls) {
        for (format in suspiciousFormats) {
            if (url.contains(format)) {
                return true
            }
        }
    }

    // Check for multiple special characters, indicative of links
    val specialChars = arrayListOf("+", "*", "#", "%", "$", "@", "&")
    val specialCharCount = specialChars.sumOf { message.count { it == specialChars.toString()[0] } }
    if (specialCharCount >= 3) {
        return true
    }

    return false
}
