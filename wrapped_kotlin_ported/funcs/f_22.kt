fun isSpam(message: String): Boolean {
    // Check for common spam keywords and phrases
    val spamKeywords = listOf("(광고)", "폭등", "상승", "수익", "마감", "종료", "공시", "이벤트", "오픈초대", "공개하겠습니다", "무료건", "이상상승", "최대", "할인", "보상", "단기수익", "VIP", "https://", "http://")
    if (spamKeywords.any { it in message }) {
        return true
    }

    // Check for excessive use of special characters
    val specialChars = Regex("[^a-zA-Z0-9가-힣\\s]").findAll(message).toList()
    if (specialChars.size / message.length.toFloat() > 0.2) {
        return true
    }

    // Check for excessive use of numbers
    val numbers = Regex("\\d+").findAll(message).toList()
    if (numbers.size / message.length.toFloat() > 0.2) {
        return true
    }

    // Check for excessive use of capital letters
    val capitalLetters = Regex("[A-Z]").findAll(message).toList()
    if (capitalLetters.size / message.length.toFloat() > 0.2) {
        return true
    }

    return false
}
