fun isSpam(message: String): Boolean {
    // Check for suspicious keywords
    val spamKeywords = listOf("투자", "적중", " 아파트", "체험반", "상승", "광고", "지급", "방법", "수익", "더이상", "최근", "모두가")
    for (keyword in spamKeywords) {
        if (keyword in message) {
            return true
        }
    }

    // Check for suspicious links
    val suspiciousLinks = listOf("bit.ly", "me2.kr", "openkakao", "ko.gl")
    for (link in suspiciousLinks) {
        if (link in message) {
            return true
        }
    }

    // Check for number patterns that might indicate a secret code, phone number or similar
    val numberPattern = Regex("\\d{6,}|\\d+(,\\d+)+|\\d+(\\.\\d+)+")
    if (numberPattern.containsMatchIn(message)) {
        return true
    }

    // Check for excessive uses of special characters
    val specialCharsPattern = Regex("[*\\[\\]()!{}\\/■?%@Δ>▲|]")
    val specialCharsCount = specialCharsPattern.findAll(message).count()
    if (specialCharsCount >= 3) {
        return true
    }

    return false
}
