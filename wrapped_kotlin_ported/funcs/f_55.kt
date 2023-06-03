fun isSpam(message: String): Boolean {
    val spamPhrases = listOf("spam", "광고", "회원", "알림", "입장", "지원", "선입금", "공짜", "특가", "회원세일", "할인", "장터")
    for (phrase in spamPhrases) {
        if (message.contains(phrase)) {
            return true
        }
    }

    val specialCharCount = message.count { it in "!@#$%^&*(),.?\":{}|<>" }
    if (specialCharCount.toDouble() / message.length > 0.5) {
        return true
    }

    val capitalCharCount = message.count { it.isUpperCase() }
    if (capitalCharCount.toDouble() / message.length > 0.5) {
        return true
    }

    val digitCount = message.count { it.isDigit() }
    if (digitCount.toDouble() / message.length > 0.4) {
        return true
    }

    val suspiciousUrls = listOf("bit.ly", "me2.kr", ".profit", "money.", "income.", "earn", "cash", "investment")
    for (url in suspiciousUrls) {
        if (message.contains(url)) {
            return true
        }
    }

    return false
}
