
fun isSpam(message: String): Boolean {
    val spamKeywords = arrayOf(
        "http://", "https://", "%", "내기", "수익", "추천", "공시", "가즈아", "외환",
        "안전", "보장", "지급", "선물", "무료", "거래", "입장", "금지", "상승", "지원금",
        "투자", "수수료", "폭등", "행복", "안내", "도와", "클릭", "확인", "이벤트", "정회원"
    )

    val messageLines = message.split("\n")

    // Check for special patterns and overly long messages
    if (messageLines.size > 4 || Regex("(.)\\1{2,}").containsMatchIn(message)) {
        return true
    }

    // Check for keywords in message
    for (keyword in spamKeywords) {
        if (keyword in message.toLowerCase()) {
            return true
        }
    }

    // Check for overly long lines in the message
    for (line in messageLines) {
        if (line.split(" ").size > 8 || line.length > 20) {
            return true
        }
    }

    return false
}

