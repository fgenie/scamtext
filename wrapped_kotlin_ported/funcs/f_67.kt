fun isSpam(text: String): Boolean {
    // Check for excessive use of special characters
    val specialCharCount = Regex("[!@#$%^&*()_=+\\[\\]{}<>:;\"'|\\\\,.?]").findAll(text).count()
    if (specialCharCount.toDouble() / text.length > 0.1) {
        return true
    }

    // Check for presence of financial numbers and shortening of amounts
    if (Regex("\\d{1,3}(,|\\.)\\d{3}").containsMatchIn(text) || Regex("\\d{1,3}(만원|천원)으로").containsMatchIn(text)) {
        return true
    }

    // Check for presence of URLs containing suspicious domain names
    val suspiciousDomains = listOf("bit.ly", "me2.kr", "han.gl", "openkakao.")
    for (domain in suspiciousDomains) {
        if (domain in text.toLowerCase()) {
            return true
        }
    }

    // Check for excessive use of up arrow character
    val upArrowCount = text.count { it == '↑' }
    if (upArrowCount.toDouble() / text.length > 0.05) {
        return true
    }

    return false
}
