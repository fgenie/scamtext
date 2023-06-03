fun isSpam(text: String): Boolean {
    // Check for specific keywords
    val keywords = listOf("광고", "무료거부", "긴급", "핵심정보", "프로젝트", "추천주", "지금 바로", "수익률", "입금")
    if (keywords.any { it in text }) {
        return true
    }

    // Check for urls with suspicious patterns
    val urlsPattern = Regex("""http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+""")
    val urls = urlsPattern.findAll(text).map { it.value }.toList()
    if (urls.isNotEmpty()) {
        for (url in urls) {
            if (listOf("bit.ly", "me2.kr", "오픈톡").any { it in url }) {
                return true
            }
        }
    }

    // Check for consecutive digits or percentages
    val digits = Regex("""\d{3,}""").findAll(text).map { it.value }.toList()
    val percentages = Regex("""\d{2,}%+""").findAll(text).map { it.value }.toList()
    if (digits.isNotEmpty() || percentages.isNotEmpty()) {
        return true
    }

    // Check for multiple special characters
    val specialChars = Regex("""[\*-_@.&+:]+""").findAll(text).map { it.value }.toList()
    if (specialChars.size > 2) {
        return true
    }

    return false
}
