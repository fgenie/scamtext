import java.util.regex.Pattern

fun isSpam(text: String): Boolean {
    val spamPatterns = arrayOf(
        "\\d{1,2}%", // Percentage discounts
        "코드[:\\:]?\\w*",
        "무료거부", // Unsubscribe keyword in Korean
        "(http(s)?://)?(bit\\.ly|me2\\.kr|vo\\.la|dokdo\\.in|tdeal\\.kr|" +
                "openkak(talk)?\\.at|kakaos?\\.co|buly\\.kr|(vvd\\.bz))\\/\\S*", // Spam URL shorteners
        "=BBQ\\+피자\\+활쿱", // Spam message
        "(광고)" // Advertising indicator
    )

    // Combine all spam patterns into a single regex pattern
    val spamPatternRe = Pattern.compile(spamPatterns.joinToString(separator = "|"), Pattern.CASE_INSENSITIVE)

    return spamPatternRe.matcher(text).find()
}
