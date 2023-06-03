fun isSpam(message: String): Boolean {
    val regex = Regex("(http[s]?://|me2|han.gl)[^ ]+")
    
    // Check for multiple occurrences of the same message
    if (message.count(message.take(10)) > 1)
        return true

    // Check for urls
    val urls = regex.findAll(message).map { it.value }.toList()
    if (urls.isNotEmpty() && urls.any { it.contains("bit.ly") || it.contains("me2.kr") || it.contains("han.gl") })
        return true

    // Check for percentages and other spam indicators
    val percentPattern = Regex("\\d+%")
    if (percentPattern.containsMatchIn(message) && (message.contains("상승") || message.contains("증가")))
        return true

    // Check for word patterns commonly found in spam messages
    val spamWords = listOf("추천주", "체험반", "무료", "상한가", "VIP")
    if (spamWords.any { message.contains(it) })
        return true

    return false
}
