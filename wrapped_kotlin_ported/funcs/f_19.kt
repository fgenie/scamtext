fun isSpam(msg: String): Boolean {
    // Check for typical spam keywords and spammy URL patterns
    val spamKeywords = arrayOf("년지원금", "진료비", "경제부기자", "안녕하세요", "지급!", "ab늪.er", "단독입수하", "보내드리", "_내일", "일 일", "특별 이벤트")
    val spammyUrlPatterns = arrayOf("(http|https)://[\\w./-]+".toRegex(), "bit\\.ly/[!-~]+".toRegex())

    // Check for spam keywords
    for (keyword in spamKeywords) {
        if (msg.contains(keyword)) {
            return true
        }
    }

    // Check for spammy URLs
    for (pattern in spammyUrlPatterns) {
        if (pattern.containsMatchIn(msg)) {
            return true
        }
    }

    return false
}
