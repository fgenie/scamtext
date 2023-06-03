fun isSpam(message: String): Boolean {
    // URL patterns
    val urlPattern1 = Regex("https?://\\S+")
    val urlPattern2 = Regex("bit\\.ly/\\S+")

    // Suspicious patterns
    val spamPattern1 = Regex("[0-9]{1,2}%?[-\\s]?[+↑]+")
    val spamPattern2 = Regex("상한가|익절가|추천주|무료체험|실현수익률")
    val spamPattern3 = Regex("\\[[^\\]]*클릭[^\\]]*]")

    // Combine all the patterns
    val patterns = listOf(urlPattern1, urlPattern2, spamPattern1, spamPattern2, spamPattern3)
    val combinedPattern = patterns.joinToString(separator = "|", transform = { it.pattern })

    // Check if any pattern is found in the message
    return combinedPattern.toRegex().containsMatchIn(message)
}
