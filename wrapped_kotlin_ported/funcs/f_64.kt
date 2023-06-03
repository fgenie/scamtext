fun isSpam(message: String): Boolean {
    var message = message.lowercase()

    // Check for common spam keywords
    val spamKeywords = arrayOf("정회원", "추천주", "클릭", "참여", "체험반", "광고", "새 가족", "※", "적립금", "방문", "무료수신거부", "적중")
    for (keyword in spamKeywords) {
        if (message.contains(keyword)) {
            return true
        }
    }

    // Check for patterns specific to spam messages
    val urlPattern = Regex("(http|https)://[a-zA-Z0-9./]+")
    val percentagePattern = Regex("\\d+%")
    val codePattern = Regex("\\w+\\d+|코드:\\w+")
    val keyPattern = Regex("key\\s*:?\\s*\\d+", RegexOption.IGNORE_CASE)

    if ((urlPattern.containsMatchIn(message) && percentagePattern.containsMatchIn(message)) ||
        (codePattern.containsMatchIn(message) || keyPattern.containsMatchIn(message))) {
        return true
    }

    return false
}
