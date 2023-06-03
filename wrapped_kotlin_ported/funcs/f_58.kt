import java.util.regex.Pattern

fun isSpam(message: String): Boolean {
    /**
     * This function takes a message as input and returns true if the message is a spam, false otherwise.
     * It checks for common spam message patterns, such as short URLs, promotional phrases, and unusual punctuation.
     */

    // Check for presence of short URLs in the message
    val shortUrlPatterns = listOf("bit\\.ly", "goo\\.gl", "me2\\.kr", "gg\\.gg", "opcn-kakao\\.com")
    if (shortUrlPatterns.any { Pattern.compile(it).matcher(message).find() }) {
        return true
    }

    // Check for promotional phrases in the message
    val promoPhrases = listOf("상한가확정", "폭등예상", "성과", "지원금", "거래량", "수수료", "무료거부")
    if (promoPhrases.any { Pattern.compile("(?i)$it").matcher(message).find() }) {
        return true
    }

    // Check for unusual punctuation in the message
    val unusualPunctuations = listOf(
        "\\*[^\n]*\\*",
        "\\-[^\n]*\\-",
        "\\^[^\n]*\\^",
        "\\_[^\n]*\\_",
        "◆[^\n]*◆",
        "▲[^\n]*▲",
        "▼[^\n]*▼",
        "▶?[^\n]*\\?"
    )
    if (unusualPunctuations.any { Pattern.compile(it).matcher(message).find() }) {
        return true
    }

    return false
}
