fun isSpam(text: String): Boolean {
    // Check for unusual numeric or special characters percentage
    val nonAlphabeticChars = text.count { !it.isLetterOrDigit() }
    val percentage = nonAlphabeticChars.toDouble() / text.length
    if (percentage > 0.3) {
        return true
    }

    // Check for excessively long alphanumeric strings (potential URLs)
    val alphanumericChunks = text.split(Regex("\\s+"))
    for (chunk in alphanumericChunks) {
        if (chunk.length > 20) {
            return true
        }
    }

    // Check for common spam phrases
    val spamPhrases = listOf("상한가", "최고이자율", "특별정보", "M반도체", "적금", "출금", "출시", "이벤트",
                    "공개", "혜택", "우대", "핵심정보", "투자", "수익률", "계좌")
    for (phrase in spamPhrases) {
        if (text.contains(phrase)) {
            return true
        }
    }

    return false
}
